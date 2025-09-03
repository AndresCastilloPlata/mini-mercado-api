# Archivo: create_tables.py
from app.database import engine, Base
from app.models import Product, User # Asegúrate de importar todos tus modelos
from dotenv import load_dotenv
import os

# Carga las variables del archivo .env para que SQLAlchemy pueda conectar
print("Cargando variables de entorno desde .env...")
load_dotenv()

print("Conectando a la base de datos y creando tablas...")
# Esta es la misma línea que comentamos, pero la ejecutamos manualmente
Base.metadata.create_all(bind=engine)

print("¡Tablas creadas con éxito en Supabase!")