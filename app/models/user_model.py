# models/user_model.py
# Define los modelos de la base de datos y los esquemas Pydantic para validación (Pydantic 2.x).

from sqlalchemy import Column, Integer, String
from app.config.config import Base
from pydantic import BaseModel, EmailStr, ConfigDict

# ==========================
# Modelo de BD (SQLAlchemy)
# ==========================
class UsuarioBD(Base):
    """
    Tabla de usuarios en la base de datos.
    """
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)

# =========================================
# Modelos Pydantic para request y response
# =========================================

class UsuarioCrear(BaseModel):
    """
    Modelo para la creación de un usuario.
    Requiere nombre y email.
    """
    nombre: str
    email: EmailStr

class UsuarioActualizar(BaseModel):
    """
    Modelo para la actualización de campos
    de un usuario (nombre y/o email).
    """
    nombre: str | None = None
    email: EmailStr | None = None

class UsuarioRespuesta(BaseModel):
    """
    Modelo para la respuesta (lectura) del usuario:
    incluye el id y habilita la conversión desde ORM.
    """
    id: int
    nombre: str
    email: EmailStr

    # Pydantic 2.x: habilita la conversión desde un objeto ORM.
    model_config = ConfigDict(from_attributes=True)
