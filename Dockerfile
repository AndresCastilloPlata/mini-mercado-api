# --- La Receta para Nuestra API ---

# 1. Ingrediente Base: Empezamos con una imagen oficial de Python 3.11 ligera.
FROM python:3.11-slim

# 2. Área de Trabajo: Creamos una carpeta llamada /code dentro del contenedor.
WORKDIR /code

# 3. Ingredientes Secos: Copiamos nuestra lista de requerimientos al contenedor.
COPY ./requirements.txt /code/requirements.txt

# 4. Preparación: Instalamos todas las librerías de la lista.
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 5. Ingrediente Principal: Copiamos toda nuestra carpeta 'app' al contenedor.
COPY ./app /code/app

# 6. Instrucción Final para Servir: Cuando el contenedor se inicie, ejecuta Uvicorn.
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]