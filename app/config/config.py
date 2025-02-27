# config/config.py
# Configuraciones de la aplicación: conexión a la base de datos, etc.

import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Cargar variables de entorno desde .env
load_dotenv()

# Leer URL de la base de datos desde las variables de entorno.
DATABASE_URL = os.getenv(
    "DATABASE_URL", "mysql+pymysql://usuario:password@localhost:3306/basedatos")

# Crear motor de conexión a MySQL.
engine = create_engine(DATABASE_URL, echo=False)

# Crear una base declarativa para los modelos.
Base = declarative_base()

# Crear una factoría de sesiones.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def inicializar_bd():
    """
    Crea las tablas en la base de datos.
    Si las tablas ya existen, no hace nada.
    """
    Base.metadata.create_all(bind=engine)


def get_db():
    """
    Provee una sesión de base de datos para inyectar en los endpoints (dependencia).
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
