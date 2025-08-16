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

