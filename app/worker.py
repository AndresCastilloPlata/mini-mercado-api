from celery import Celery
import time

# Configura Celery para usar Redis como "tablón de anuncios" (broker)
celery_app = Celery(
    'tasks',
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0'
)

@celery_app.task
def send_welcome_email(email: str):
    """
    Una tarea simulada que "envía" un email de bienvenida.
    En un proyecto real, aquí iría el código para conectarse a un servicio de email.
    """
    print(f"Preparando para enviar email a {email}...")
    # Simulamos que la tarea es lenta
    time.sleep(5) 
    print(f"¡Email de bienvenida enviado a {email}!")
    return {"email": email, "status": "enviado"}