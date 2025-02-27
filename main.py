# main.py
# Punto de entrada principal de la aplicación FastAPI

from fastapi import FastAPI
from app.config.config import inicializar_bd
from app.routes.user_routes import user_router
from app.middlewares.logging_middleware import LoggingMiddleware

# Crea la instancia de la aplicación FastAPI.
app = FastAPI(
    title="API de Usuarios",
    description="API para la gestión de usuarios usando FastAPI y MySQL.",
    version="1.0.0"
)

# Inicializa la base de datos al arrancar la aplicación.
inicializar_bd()

# Agrega un middleware personalizado (por ejemplo, para logging).
app.add_middleware(LoggingMiddleware)

# Incluye las rutas de usuarios.
app.include_router(user_router)

# Endpoint de prueba para verificar que la API está corriendo.


@app.get("/", tags=["Inicio"])
def inicio():
    """
    Endpoint principal para verificar que la API está en funcionamiento.
    Retorna un mensaje de bienvenida.
    """
    return {"mensaje": "Bienvenido a la API de Usuarios"}
