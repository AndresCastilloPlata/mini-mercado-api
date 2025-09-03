# Dockerfile (Versión de prueba)
FROM python:3.11-slim
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app/main.py /code/app/main.py
# Necesitamos un __init__.py vacío para que 'app.main' funcione
RUN touch /code/app/__init__.py
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]