# utils/logger.py
# Configuración de logging para el proyecto.

import logging

# Configurar el logger
logger = logging.getLogger("py_api_usuario")
logger.setLevel(logging.INFO)

# Formato del mensaje
formato = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# Handler para la salida en consola
console_handler = logging.StreamHandler()
console_handler.setFormatter(formato)
logger.addHandler(console_handler)
