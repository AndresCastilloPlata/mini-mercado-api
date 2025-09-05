# 📦 Mini-Mercado API 🏪

¡Bienvenido a la API de Mini-Mercado! Este proyecto es una API RESTful robusta y completa para gestionar el inventario de un pequeño e-commerce, construida con Python, FastAPI y PostgreSQL.

Este proyecto fue desarrollado como parte de un plan de estudio intensivo para dominar el desarrollo backend con Python, cubriendo desde los fundamentos hasta conceptos de nivel experto como autenticación, bases de datos y pruebas automatizadas.

---

## ✨ Características Principales

* **API RESTful Completa:** Operaciones CRUD (Crear, Leer, Actualizar, Eliminar) para productos.
* **Autenticación Segura:** Sistema de registro y login basado en Tokens JWT. Rutas protegidas para operaciones sensibles.
* **Base de Datos Profesional:** Persistencia de datos con PostgreSQL, gestionado con el ORM SQLAlchemy.
* **Validación de Datos:** Uso de Pydantic para una validación de datos robusta y automática en la entrada y salida de la API.
* **Entorno Contenerizado:** La base de datos se ejecuta en un contenedor de Docker para un desarrollo limpio y reproducible.
* **Suite de Pruebas:** Pruebas automatizadas con Pytest para garantizar la fiabilidad y estabilidad del código.
* **Documentación Automática:** Documentación interactiva de la API generada automáticamente por FastAPI (Swagger UI y ReDoc).

---

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3.11+
* **Framework:** FastAPI
* **Base de Datos:** PostgreSQL
* **ORM:** SQLAlchemy
* **Validación de Datos:** Pydantic
* **Seguridad:** Passlib (para hashing), Python-JOSE (para JWTs)
* **Pruebas:** Pytest
* **Servidor ASGI:** Uvicorn
* **Contenerización:** Docker (Docker Compose)

---

## 🚀 Cómo Empezar

Sigue estos pasos para levantar el proyecto en tu entorno local.

### **Pre-requisitos**

* Python 3.11 o superior
* Docker y Docker Compose
* Git

### **Instalación y Ejecución**

1.  **Clona el repositorio:**
    ```bash
    git clone [https://github.com/AndresCastilloPlata/mini-mercado-api](https://github.com/AndresCastilloPlata/mini-mercado-api.git)
    cd mini-mercado-api
    ```

2.  **Crea y activa un entorno virtual:**
    ```bash
    python -m venv venv
    # En Windows
    .\venv\Scripts\activate
    # En Mac/Linux
    source venv/bin/activate
    ```

3.  **Instala las dependencias de Python:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Nota: Asegúrate de tener un archivo `requirements.txt`. Puedes crearlo con `pip freeze > requirements.txt`)*

4.  **Levanta la base de datos con Docker:**
    ```bash
    docker-compose up -d
    ```

5.  **Ejecuta la aplicación FastAPI:**
    ```bash
    uvicorn app.main:app --reload --port 8080
    ```

¡Listo! La API estará corriendo en `http://127.0.0.1:8080`.

### **Documentación Interactiva**

* **Swagger UI:** [http://127.0.0.1:8080/docs](http://127.0.0.1:8080/docs)
* **ReDoc:** [http://127.0.0.1:8080/redoc](http://127.0.0.1:8080/redoc)

---

## 🧪 Cómo Ejecutar las Pruebas

Para verificar que todo funciona correctamente, ejecuta la suite de pruebas automatizadas:

```bash
pytest
```

## ☁️ Despliegue

La API está desplegada en **Google Cloud Run** y está disponible públicamente en la siguiente URL:

**[https://mini-mercado-api-1047555500556.us-central1.run.app/docs](https://mini-mercado-api-1047555500556.us-central1.run.app/docs)**

La base de datos PostgreSQL está alojada en **Supabase** y el broker de Redis en **Upstash**, ambos en sus respectivos niveles gratuitos. El pipeline de CI/CD con **GitHub Actions** asegura la calidad del código en cada commit.