# 🚀 B1Boost: English Learning & Vocabulary Platform

**B1Boost** es una aplicación multiplataforma diseñada para impulsar el aprendizaje del idioma inglés, facilitando la transición del nivel **A2 al B1**. A través de tarjetas de estudio dinámicas y reglas gramaticales, la plataforma ofrece una interfaz ligera y rápida para repasar conceptos clave.

El proyecto está diseñado de forma modular, permitiendo interactuar con el sistema a través de **tres alternativas de ejecución** según las necesidades del usuario o desarrollador.

---

## 🛠️ Tecnologías Utilizadas

* **Python 3.11+**: Lenguaje de programación base.
* **FastAPI**: Framework web de alto rendimiento para las versiones API y Web.
* **Uvicorn**: Servidor ASGI para el entorno local.
* **Jinja2**: Motor de plantillas para renderizar la interfaz HTML.
* **Render**: Infraestructura en la nube para el despliegue público.

---

## 🕹️ Tres Alternativas de Ejecución

Este repositorio está estructurado para correr el proyecto de tres maneras diferentes:

### 1. Versión por Consola (`main_consola.py`)
Diseñada para un consumo ligero de recursos directamente desde la terminal. Selecciona de forma interactiva y aleatoria las tarjetas de inglés y las muestra en texto plano. Ideal para repasos rápidos mientras se trabaja en la terminal.

* **Comando para correrlo:**

      python main_consola.py


#   2. Versión API Básica (main_api_basica.py)

Levanta un backend local con FastAPI que expone los datos en formato JSON. Es la base ideal para conectar este proyecto en el futuro con otras aplicaciones, flujos de automatización (RPA) o interfaces móviles.

Comando para correrlo:

    python -m uvicorn main_api_basica:app --reload


Acceso: Entrega los datos puros en formato JSON al ingresar a http://127.0.0.1:8000/.

# 3. Versión Web en la Nube (Render + main.py)

La experiencia de usuario completa. Combina la lógica de FastAPI con una interfaz visual responsiva en HTML y CSS a través de Jinja2. Está desplegada de forma pública en internet gracias a los servidores de Render, contando con integración continua directa con este repositorio.

Enlace de Producción: Tu Enlace Aquí (Modifica con tu link real)


# 📁 Estructura del Proyecto


├── data.py                 # Diccionarios y listas con las tarjetas de estudio
├── main_consola.py         # Alternativa 1: Ejecución interactiva por terminal
├── main_api_basica.py      # Alternativa 2: Backend local con respuestas JSON
├── main.py                 # Alternativa 3: Cerebro de la plataforma web en Render
├── requirements.txt        # Dependencias necesarias para el servidor
├── templates/
│   └── index.html          # Interfaz visual para la versión web
└── README.md               # Documentación del proyecto


# 🚀 Despliegue Continuo (CI/CD)
La versión web está conectada a Render. Cada vez que se realiza un ajuste en el código local o se agregan nuevas tarjetas en data.py, el servidor en producción se actualiza automáticamente ejecutando estos comandos en la terminal local:


        git add .
        git commit -m "feat: actualización de contenido didáctico"
        git push origin main


Proyecto desarrollado de forma estructurada como parte del portafolio de desarrollo de software y automatización con Python.

