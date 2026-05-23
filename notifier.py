import random
from plyer import notification


def lanzar_alerta(lista_tarjetas):
    tarjeta = random.choice(lista_tarjetas)

    notification.notify(
        title="✨ B1Boost",
        message=f"💡 {tarjeta['tema']}\n\n{tarjeta['regla']}",
        app_name="B1Boost",  # Evita que Windows bloquee la alerta por falta de origen
        timeout=1800,
    )