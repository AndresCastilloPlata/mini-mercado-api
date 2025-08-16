from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app, get_db
from app.database import Base
import pytest

# --- Configuración de la Base de Datos de Prueba ---
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# --- Sobrescribir la Dependencia de la Base de Datos ---
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()
        
# Le decimos a nuestra app que use la BD de prueba en lugar de la de producción
app.dependency_overrides[get_db] = override_get_db


# --- Creación del Cliente de Prueba ---
# Este 'client' es nuestro "navegador" para hacer peticiones a la API
client = TestClient(app)

# --- Lógica de Prueba ---
# Esto se ejecuta antes de cada prueba para tener una base de datos limpia
@pytest.fixture(autouse=True)
def setup_and_teardown_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)




def test_read_products_empty():
    # Hacemos una petición GET a la ruta /products
    response = client.get("/products")

    # Verificamos que todo salió bien
    assert response.status_code == 200
    # Verificamos que la respuesta es una lista vacía (porque la BD está limpia)
    assert response.json() == []



def test_create_user():
    # El robot prepara los datos para una nueva cuenta
    user_data = {"email": "test@gmail.com", "password": "password1234"}
    
    # El robot hace la petición POST para registrarse
    response = client.post("/users/", json=user_data)
    
    # El robot revisa si la respuesta es la correcta
    assert response.status_code == 200 # FastAPI devuelve 200 por defecto aquí
    
    response_data = response.json()
    assert response_data["email"] == user_data["email"]
    assert "id" in response_data
    # ¡OJO! Verificamos que la contraseña NO se devuelva en la respuesta
    assert "password" not in response_data 
    
    
    
def test_login_for_access_token():
    # Primero, necesitamos un usuario en la BD de prueba
    user_data = {"email": "login@gmail.com", "password": "password1234"}
    client.post("/users/", json=user_data)
    
    # El robot intenta hacer login con los datos correctos
    login_data = {"username": "login@gmail.com", "password": "password1234"}
    # OJO: para el token, FastAPI espera datos de formulario, no JSON
    response = client.post("/token", data=login_data)
    
    # El robot revisa
    assert response.status_code == 200
    response_data = response.json()
    assert "access_token" in response_data
    assert response_data["token_type"] == "bearer"



def test_create_product_unauthorized():
    product_data = {"name": "Test Product", "price": 10.0, "stock": 100}
    
    # El robot intenta crear el producto SIN la cabecera de autorización
    response = client.post("/products", json=product_data)
    
    # El robot comprueba que lo han rechazado correctamente
    assert response.status_code == 401 # 401 Unauthorized


def test_create_product_authorized():
    # 1. El robot crea una cuenta
    user_data = {"email": "auth@gmail.com", "password": "password1234"}
    client.post("/users/", json=user_data)

    # 2. El robot hace login para obtener su "pulsera" (token)
    login_data = {"username": "auth@gmail.com", "password": "password1234"}
    response = client.post("/token", data=login_data)
    token = response.json()["access_token"]

    # 3. El robot prepara su "pase VIP" (la cabecera de autorización)
    headers = {"Authorization": f"Bearer {token}"}
    
    # 4. El robot prepara los datos del producto
    product_data = {"name": "Authorized Product", "price": 99.99, "stock": 50}

    # 5. El robot entra a la zona VIP mostrando su pase
    response = client.post("/products", json=product_data, headers=headers)

    # 6. El robot revisa que todo haya salido perfecto
    assert response.status_code == 201 # 201 Created
    response_data = response.json()
    assert response_data["name"] == product_data["name"]



def test_update_product_authorized():
    # --- PREPARACIÓN ---
    # 1. Crear usuario y loguearse para obtener el token
    client.post("/users/", json={"email": "update@gmail.com", "password": "password1234"})
    login_response = client.post("/token", data={"username": "update@gmail.com", "password": "password1234"})
    token = login_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # 2. Crear un producto inicial para tener algo que actualizar
    initial_product_data = {"name": "Old Name", "price": 10.0, "stock": 10}
    create_response = client.post("/products", json=initial_product_data, headers=headers)
    assert create_response.status_code == 201
    product_id = create_response.json()["id"]

    # --- ACCIÓN ---
    # 3. Preparar los nuevos datos y hacer la petición PUT
    updated_product_data = {"name": "New Name", "price": 99.99, "stock": 5}
    response = client.put(f"/products/{product_id}", json=updated_product_data, headers=headers)

    # --- VERIFICACIÓN ---
    # 4. Comprobar que la actualización fue exitosa y los datos cambiaron
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["name"] == "New Name"
    assert response_data["price"] == 99.99
    assert response_data["stock"] == 5
    assert response_data["id"] == product_id



def test_delete_product_authorized():
    # --- PREPARACIÓN ---
    # 1. Crear usuario, loguearse y obtener token
    client.post("/users/", json={"email": "delete@gmail.com", "password": "password1234"})
    login_response = client.post("/token", data={"username": "delete@gmail.com", "password": "password1234"})
    token = login_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # 2. Crear un producto para tener algo que eliminar
    product_to_delete = {"name": "To Be Deleted", "price": 1.0, "stock": 1}
    create_response = client.post("/products", json=product_to_delete, headers=headers)
    assert create_response.status_code == 201
    product_id = create_response.json()["id"]

    # --- ACCIÓN ---
    # 3. Hacer la petición DELETE
    response = client.delete(f"/products/{product_id}", headers=headers)

    # --- VERIFICACIÓN ---
    # 4. Comprobar que la eliminación fue exitosa
    assert response.status_code == 200
    assert response.json() == {"mensaje": f"Producto con ID {product_id} eliminado con éxito"}

    # 5. ¡El paso crucial! Verificar que el producto ya no existe
    get_response = client.get(f"/products/{product_id}")
    assert get_response.status_code == 404 # 404 Not Found

