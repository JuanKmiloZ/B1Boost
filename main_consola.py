import random
import time
from data import TARJETAS
from notifier import lanzar_alerta




while True:
    lanzar_alerta(TARJETAS)
    tiempo_sorpresa=random.randit(5400,9000)
    time.sleep(tiempo_sorpresa)

