# Archivo: api.py

from fastapi import FastAPI, HTTPException
import json # <--- 1. ASEGÚRATE DE AÑADIR ESTA LÍNEA

# ... (La creación de la 'app' de FastAPI se queda igual)
app = FastAPI(
    title="Mini-Mercado API", 
    version="0.0.1",
    description="La API para gestionar el inventario de nuestro Mini-Mercado"
)

# --- LÓGICA DE DATOS ---
# 2. AÑADE ESTE BLOQUE DE CÓDIGO COMPLETO
def cargar_inventario():
    """Carga el inventario desde inventory.json."""
    try:
        with open('inventory.json', 'r') as archivo:
            return json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        # Si el archivo no existe o está vacío/corrupto, devolvemos una lista vacía
        return []

# Cargamos los datos en una variable global al iniciar la aplicación
inventario = cargar_inventario()
# --- FIN DEL BLOQUE AÑADIDO ---


# ... (Tus endpoints @app.get("/") y @app.get("/health") se quedan igual)
@app.get("/")
def leer_raiz():
    """
    Este es el endpoint raíz de la API.
    Devuelve un mensaje de bienvenida.
    """
    return {"mensaje": "Bienvenido a la API del Mini-Mercado"}

@app.get("/health")
def check_health():
    """Endpoint para verificar que la API está viva."""
    return {"status": "ok"}


# --- ENDPOINT PARA PRODUCTOS ---
@app.get("/products")
def get_products():
    """
    Devuelve la lista completa de productos del inventario.
    """
    # FastAPI convierte automáticamente esta lista de Python a JSON
    return inventario


# --- ENDPOINT PARA UN PRODUCTO ---
@app.get("/products/{product_id}")
def get_product_by_id(product_id: int):
    """
    Busca y devuelve un solo producto basado en su ID.
    """
    # Recorremos cada 'producto' (que es un diccionario) en nuestra lista 'inventario'
    for producto in inventario:
        # Comparamos el VALOR de la clave 'id' de ese diccionario con el ID que buscamos
        if producto['id'] == product_id:
            # Si coinciden, hemos encontrado nuestro producto. Lo retornamos.
            return producto
    
    # Si el bucle termina y nunca retornamos nada, el producto no fue encontrado.
    raise HTTPException(status_code=404, detail=f"Producto con ID {product_id} no encontrado")


  