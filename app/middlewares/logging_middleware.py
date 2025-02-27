# middlewares/logging_middleware.py
# Ejemplo de middleware que loguea cada solicitud y respuesta

import time
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from app.utils.logger import logger


class LoggingMiddleware(BaseHTTPMiddleware):
    """
    Middleware personalizado para registrar información
    de cada petición entrante y su tiempo de respuesta.
    """

    async def dispatch(self, request: Request, call_next):
        inicio = time.time()
        response = await call_next(request)
        fin = time.time()

        # Registrar la información en el logger
        logger.info(
            f"METODO={request.method} PATH={request.url.path} "
            f"STATUS_CODE={response.status_code} "
            f"TIEMPO={(fin - inicio):.4f} segundos"
        )
        return response
