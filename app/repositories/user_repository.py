# repositories/user_repository.py
# Se encarga de la interacción directa con la base de datos para los usuarios.

from sqlalchemy.orm import Session
from app.models.user_model import UsuarioBD


def crear_usuario(db: Session, nombre: str, email: str) -> UsuarioBD:
    """
    Crea un nuevo registro de usuario en la base de datos.
    """
    nuevo_usuario = UsuarioBD(nombre=nombre, email=email)
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario


def listar_usuarios(db: Session) -> list[UsuarioBD]:
    """
    Retorna todos los usuarios registrados.
    """
    return db.query(UsuarioBD).all()


def obtener_usuario(db: Session, usuario_id: int) -> UsuarioBD | None:
    """
    Retorna un usuario por su ID, o None si no existe.
    """
    return db.query(UsuarioBD).filter(UsuarioBD.id == usuario_id).first()


def obtener_usuario_por_email(db: Session, email: str) -> UsuarioBD | None:
    """
    Retorna un usuario por su email, o None si no existe.
    """
    return db.query(UsuarioBD).filter(UsuarioBD.email == email).first()


def actualizar_usuario(db: Session, usuario: UsuarioBD, nombre: str | None, email: str | None) -> UsuarioBD:
    """
    Actualiza un usuario existente en la base de datos.
    """
    if nombre is not None:
        usuario.nombre = nombre
    if email is not None:
        usuario.email = email
    db.commit()
    db.refresh(usuario)
    return usuario


def eliminar_usuario(db: Session, usuario: UsuarioBD) -> bool:
    """
    Elimina un usuario de la base de datos.
    """
    db.delete(usuario)
    db.commit()
    return True
