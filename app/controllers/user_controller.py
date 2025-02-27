# controllers/user_controller.py
# Controlador de usuarios: maneja la lógica de cada endpoint.
# Se apoya en los servicios para realizar la lógica de negocio.

from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.services.user_service import crear_usuario_service, listar_usuarios_service, obtener_usuario_service, actualizar_usuario_service, eliminar_usuario_service
from app.models.user_model import UsuarioCrear, UsuarioActualizar


def crear_usuario_controller(db: Session, datos_usuario: UsuarioCrear):
    """
    Controlador para crear un nuevo usuario.
    Valida datos y llama al servicio correspondiente.
    """
    usuario_creado = crear_usuario_service(db, datos_usuario)
    if not usuario_creado:
        # Si el servicio retorna None, significa que hubo un error (por ejemplo, usuario ya existe).
        raise HTTPException(
            status_code=400, detail="No se pudo crear el usuario.")
    return usuario_creado


def listar_usuarios_controller(db: Session):
    """
    Controlador para listar todos los usuarios.
    """
    return listar_usuarios_service(db)


def obtener_usuario_controller(db: Session, usuario_id: int):
    """
    Controlador para obtener un usuario por su ID.
    """
    usuario = obtener_usuario_service(db, usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado.")
    return usuario


def actualizar_usuario_controller(db: Session, usuario_id: int, datos_usuario: UsuarioActualizar):
    """
    Controlador para actualizar un usuario existente.
    """
    usuario_actualizado = actualizar_usuario_service(
        db, usuario_id, datos_usuario)
    if not usuario_actualizado:
        raise HTTPException(
            status_code=404, detail="Usuario no encontrado o no se pudo actualizar.")
    return usuario_actualizado


def eliminar_usuario_controller(db: Session, usuario_id: int):
    """
    Controlador para eliminar un usuario por su ID.
    """
    resultado = eliminar_usuario_service(db, usuario_id)
    if not resultado:
        raise HTTPException(
            status_code=404, detail="Usuario no encontrado o no se pudo eliminar.")
    return {"mensaje": "Usuario eliminado con éxito."}
