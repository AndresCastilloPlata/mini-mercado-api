# Archivo: app/redis_client.py
import redis
import json
from .config import settings

# Nos conectamos a Redis. 
# Usamos db=1 para separar los datos del caché de los de Celery (que usan db=0 por defecto).
# decode_responses=True para que nos devuelva strings en lugar de bytes.
redis_client = redis.Redis(settings.DATABASE_URL, db=1, decode_responses=True)

def get_from_cache(key: str):
    """Obtiene un valor del caché."""
    value = redis_client.get(key)
    if value:
        return json.loads(value)
    return None

def set_in_cache(key: str, value: dict, expire: int = 3600):
    """Guarda un valor en el caché con un tiempo de expiración (en segundos)."""
    redis_client.setex(key, expire, json.dumps(value))