# tests/test_user.py
# Ejemplo de pruebas unitarias para el CRUD de usuarios usando pytest y la base de datos en memoria (opcional).

import pytest
from fastapi.testclient import TestClient
from main import app
from app.config.config import SessionLocal, Base, engine

# Crear un cliente de pruebas
client = TestClient(app)

@pytest.fixture(autouse=True)
def setup_db():
    """
    Configura la base de datos para pruebas.
    Se ejecuta antes de cada test.
    """
    # En caso de usar una BD distinta para test, ajusta la URL en config.
    Base.metadata.drop_all(bind=engine)   # Limpia
    Base.metadata.create_all(bind=engine) # Crea
    yield
    # Base.metadata.drop_all(bind=engine)   # Opcional, si quieres dejar sin tablas al final

def test_crear_usuario():
    """
    Prueba la creación de un usuario.
    """
    # Datos de ejemplo
    data = {
        "nombre": "Juan Perez",
        "email": "juan@example.com"
    }
    response = client.post("/usuarios/", json=data)
    assert response.status_code == 200
    json_resp = response.json()
    assert "usuario_creado" in json_resp

def test_listar_usuarios():
    """
    Prueba la obtención de la lista de usuarios.
    """
    response = client.get("/usuarios/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_obtener_usuario():
    """
    Prueba la obtención de un usuario por ID.
    """
    # Crear un usuario primero
    data = {
        "nombre": "Maria Gomez",
        "email": "maria@example.com"
    }
    create_resp = client.post("/usuarios/", json=data)
    user_id = create_resp.json()["usuario_creado"]["id"]

    # Obtener el usuario
    get_resp = client.get(f"/usuarios/{user_id}")
    assert get_resp.status_code == 200
    assert get_resp.json()["usuario"]["nombre"] == "Maria Gomez"

def test_actualizar_usuario():
    """
    Prueba la actualización de un usuario existente.
    """
    # Crear un usuario
    data = {
        "nombre": "Pedro",
        "email": "pedro@example.com"
    }
    create_resp = client.post("/usuarios/", json=data)
    user_id = create_resp.json()["usuario_creado"]["id"]

    # Actualizar el usuario
    update_data = {
        "nombre": "Pedro Actualizado",
        "email": "pedro2@example.com"
    }
    update_resp = client.put(f"/usuarios/{user_id}", json=update_data)
    assert update_resp.status_code == 200
    assert update_resp.json()["usuario_actualizado"]["nombre"] == "Pedro Actualizado"

def test_eliminar_usuario():
    """
    Prueba la eliminación de un usuario.
    """
    # Crear un usuario
    data = {
        "nombre": "Usuario Borrar",
        "email": "delete@example.com"
    }
    create_resp = client.post("/usuarios/", json=data)
    user_id = create_resp.json()["usuario_creado"]["id"]

    # Eliminar el usuario
    delete_resp = client.delete(f"/usuarios/{user_id}")
    assert delete_resp.status_code == 200
    assert delete_resp.json()["mensaje"] == "Usuario eliminado con éxito."
