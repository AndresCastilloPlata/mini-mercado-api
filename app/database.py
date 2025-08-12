from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# La dirección de nuestra base de datos en Docker
DATABASE_URL = "postgresql://user:password@localhost/minimercado_db"

# Creamos el "motor" de la base de datos
engine = create_engine(DATABASE_URL)

# Creamos una fábrica de sesiones (nuestros "carritos de biblioteca")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Una clase base que nuestros modelos usarán para heredar
Base = declarative_base()