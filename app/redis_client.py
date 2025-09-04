# Archivo: app/redis_client.py
import redis
import json
from .config import settings
import os

# Esta es una forma más explícita y segura de conectarse a Redis en producción
# Se asegura de forzar la conexión SSL (requerida por Upstash).
redis_client = redis.from_url(settings.REDIS_URL, db=1, decode_responses=True, ssl_cert_reqs=None)

def get_from_cache(key: str):
    """Obtiene un valor del caché."""
    value = redis_client.get(key)
    if value:
        return json.loads(value)
    return None

def set_in_cache(key: str, value: dict, expire: int = 3600):
    """Guarda un valor en el caché con un tiempo de expiración (en segundos)."""
    redis_client.setex(key, expire, json.dumps(value))