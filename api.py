# Archivo: api.py

from fastapi import FastAPI

# 1. Creamos una instancia de la aplicación FastAPI
#    Esto será el punto central de toda nuestra API.
app = FastAPI(
    title="Mini-Mercado API", 
    version="0.0.1",
    description="La API para gestionar el inventario de nuestro Mini-Mercado"
)


# 2. Definimos nuestro primer endpoint usando un "decorador"
#    @app.get("/") le dice a FastAPI que la función de abajo
#    manejará las peticiones GET a la URL raíz ("/").
@app.get("/")
def leer_raiz():
    """
    Este es el endpoint raíz de la API.
    Devuelve un mensaje de bienvenida.
    """
    return {"mensaje": "Bienvenido a la API del Mini-Mercado"}

# AÑADE ESTE NUEVO BLOQUE DE CÓDIGO
@app.get("/health")
def check_health():
    """Endpoint para verificar que la API está viva."""
    return {"status": "ok"}