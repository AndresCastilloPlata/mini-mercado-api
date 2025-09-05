# Archivo: app/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    REDIS_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    # Usamos 'Config' en lugar de 'model_config' para mayor compatibilidad
    class Config:
        # Esta línea es la clave, busca el archivo si existe
        env_file = ".env"
        # Esta línea indica que si hay un error, no falle silenciosamente
        env_file_encoding = 'utf-8'

settings = Settings()