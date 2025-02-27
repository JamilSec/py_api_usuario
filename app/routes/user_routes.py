from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.config.config import get_db
from app.controllers.user_controller import (
    crear_usuario_controller,
    listar_usuarios_controller,
    obtener_usuario_controller,
    actualizar_usuario_controller,
    eliminar_usuario_controller
)
from app.models.user_model import UsuarioCrear, UsuarioActualizar, UsuarioRespuesta

user_router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"]
)


@user_router.post("/", response_model=dict)
def crear_usuario_endpoint(datos_usuario: UsuarioCrear, db: Session = Depends(get_db)):
    usuario_bd = crear_usuario_controller(db, datos_usuario)
    usuario_pydantic = UsuarioRespuesta.model_validate(usuario_bd)
    return {
        "usuario_creado": usuario_pydantic
    }


@user_router.get("/", response_model=list[UsuarioRespuesta])
def listar_usuarios_endpoint(db: Session = Depends(get_db)):
    """
    Endpoint para listar todos los usuarios.
    """
    usuarios_bd = listar_usuarios_controller(db)
    # Convertir cada objeto ORM en un modelo Pydantic
    return [UsuarioRespuesta.model_validate(u) for u in usuarios_bd]


# IMPORTANTE: Quita "usuarios/" del path:
@user_router.get("/{usuario_id}", response_model=dict)
def obtener_usuario_endpoint(usuario_id: int, db: Session = Depends(get_db)):
    usuario_bd = obtener_usuario_controller(db, usuario_id)
    # Envolverlo según lo que tu test espera
    return {
        "usuario": UsuarioRespuesta.model_validate(usuario_bd)
    }


@user_router.put("/{usuario_id}", response_model=dict)
def actualizar_usuario_endpoint(usuario_id: int, datos_usuario: UsuarioActualizar, db: Session = Depends(get_db)):
    usuario_bd = actualizar_usuario_controller(db, usuario_id, datos_usuario)
    return {
        "usuario_actualizado": UsuarioRespuesta.model_validate(usuario_bd)
    }


@user_router.delete("/{usuario_id}", response_model=dict)
def eliminar_usuario_endpoint(usuario_id: int, db: Session = Depends(get_db)):
    respuesta = eliminar_usuario_controller(db, usuario_id)
    return respuesta
