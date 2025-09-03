# Archivo: app/main.py (Versión de prueba)
from fastapi import FastAPI

app = FastAPI(title="Prueba de Despliegue")

@app.get("/")
def read_root():
    return {"Hola": "Mundo"}