from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Aquí defines todas las variables que esperas leer del archivo .env
    DATABASE_URL: str
    REDIS_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    # Esta línea le dice a Pydantic que lea las variables de entorno en produccion
    model_config = SettingsConfigDict()

# Creamos una única instancia que usaremos en toda la aplicación
settings = Settings()