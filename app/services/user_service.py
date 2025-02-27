# services/user_service.py
# Contiene la lógica de negocio de usuarios. Valida condiciones antes de interactuar con el repositorio.

from sqlalchemy.orm import Session
from app.repositories.user_repository import (
    crear_usuario,
    listar_usuarios,
    obtener_usuario,
    obtener_usuario_por_email,
    actualizar_usuario,
    eliminar_usuario
)
from app.models.user_model import UsuarioCrear, UsuarioActualizar


def crear_usuario_service(db: Session, datos_usuario: UsuarioCrear):
    """
    Lógica de negocio para la creación de un usuario.
    Se valida si el email ya existe antes de crearlo.
    """
    usuario_existente = obtener_usuario_por_email(db, datos_usuario.email)
    if usuario_existente:
        # Ya existe un usuario con ese correo
        return None
    return crear_usuario(db, datos_usuario.nombre, datos_usuario.email)


def listar_usuarios_service(db: Session):
    """
    Lógica de negocio para listar todos los usuarios.
    """
    return listar_usuarios(db)


def obtener_usuario_service(db: Session, usuario_id: int):
    """
    Lógica de negocio para obtener un usuario por ID.
    """
    return obtener_usuario(db, usuario_id)


def actualizar_usuario_service(db: Session, usuario_id: int, datos_usuario: UsuarioActualizar):
    """
    Lógica de negocio para actualizar un usuario.
    """
    usuario_en_bd = obtener_usuario(db, usuario_id)
    if not usuario_en_bd:
        return None
    # Validar si el nuevo email ya existe en otro usuario
    if datos_usuario.email:
        usuario_con_mismo_email = obtener_usuario_por_email(
            db, datos_usuario.email)
        if usuario_con_mismo_email and usuario_con_mismo_email.id != usuario_id:
            return None  # No se puede actualizar porque el email ya lo usa otro usuario
    usuario_actualizado = actualizar_usuario(
        db,
        usuario_en_bd,
        datos_usuario.nombre,
        datos_usuario.email
    )
    return usuario_actualizado


def eliminar_usuario_service(db: Session, usuario_id: int):
    """
    Lógica de negocio para eliminar un usuario.
    """
    usuario_en_bd = obtener_usuario(db, usuario_id)
    if not usuario_en_bd:
        return None
    return eliminar_usuario(db, usuario_en_bd)
