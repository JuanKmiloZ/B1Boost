import random
from data import TARJETAS
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# 1. Creamos la aplicación de FastAPI
app = FastAPI()

# 2. Le decimos a FastAPI que busque las pantallas HTML en la carpeta "templates"
templates = Jinja2Templates(directory="templates")


# 3. Ruta principal: Compatible con la exigencia de 'request' de tu versión
@app.get("/", response_class=HTMLResponse)
def inicio(request: Request):
    return templates.TemplateResponse(request, "index.html")


# 4. Ruta de datos: Esta sigue entregando las tarjetas en formato JSON de fondo
@app.get("/tarjeta")
def obtener_tarjeta():
    return random.choice(TARJETAS)
