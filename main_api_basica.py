import random
import time
from data import TARJETAS
from fastapi import FastAPI

#Creamos la aplicacion de FastAPI

app=FastAPI()

#Ruta principal (cuando entras a la página base)

@app.get("/")
def inicio():
    return {
        "mensaje": "¡Bienvenido a la API de B1Boost!"
        }

# Ruta que elige y entrega las tarjetas en formato JSON
@app.get("/tarjeta")
def obtener_tarjeta():
    tarjeta = random.choice(TARJETAS)
    return tarjeta
