# py_api_usuario
¡Bienvenido/a! Este es un proyecto de `FastAPI` con una estructura modular para gestionar un CRUD de usuarios, pruebas unitarias con `pytest` y pruebas de rendimiento con `JMeter`.

## Tabla de Contenidos
- [Requisitos](#requisitos)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Instalación](#instalacion)
- [Ejecución de la Aplicación](#ejecucion-de-la-aplicacion)
- [Pruebas Unitarias](#pruebas-unitarias)
- [Pruebas de Carga con JMeter](#pruebas-de-carga-con-jmeter)

## Requisitos

- Python 3.10 o superior.
- (Opcional) Entorno virtual (puedes usar `venv`, `conda`, `pipenv` o `poetry`).
- MySQL o una base de datos compatible.
- (Opcional) JMeter si deseas correr pruebas de rendimiento.

## Estructura del Proyecto

```scss
py_api_usuario/
├─ app/
│  ├─ config/        # Configuración de la BD, etc.
│  |  ├─ config.py   
│  ├─ controllers/   # Controladores para la lógica de cada endpoint
│  |  ├─ usuario.constroller.py   
│  ├─ middlewares/   # Middlewares personalizados
│  |  ├─ iniciosesion.middleware.py   
│  ├─ models/        # Modelos de BD (SQLAlchemy) y Pydantic
│  |  ├─ user_model.py   
│  ├─ repositories/  # Lógica de acceso a datos
│  |  ├─ user_respository.py   
│  ├─ routes/        # Definición de endpoints (paths)
│  |  ├─ user_routes.py   
│  ├─ services/      # Lógica de negocio
│  |  ├─ user_service.py   
│  └─ utils/         # Utilidades (logging, helpers)
│  |  ├─ logger.py
│  ├─ __init__.py   
├─ tests/
│  ├─ user
│  |  ├─ __init__.py
│  |  ├─ test_user.py # Pruebas unitarias (pytest)
│  └─ __init__.py  
├─ main.py           # Punto de entrada principal
├─ requirements.txt  # Dependencias del proyecto
├─ .env              # Variables de entorno (DB, etc.)
└─ README.md         # Documentación de proyecto
```

## Instalación
1. Clonar el repositorio:
    ```bash
    git clone https://github.com/JamilSec/py_api_usuario.git
    ```
2. Crear un entorno virtual (opcional pero recomendado):
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Linux/Mac
    # o en Windows:
    # .\venv\Scripts\activate
    ```
3. Instalar las dependencias:
    ```bash
    pip install -r requirements.txt
    ```
4. Configurar las variables de entorno en un archivo `.env` si es necesario (p.ej. `DATABASE_URL`). Ejemplo:
    ```bash
    DATABASE_URL=mysql+pymysql://usuario:password@localhost:3306/bd_usuarios
    ```

## Ejecución de la Aplicación
1. Iniciar el servidor con Uvicorn en modo desarrollo:
    ```bash
    uvicorn main:app --reload
    ```
2. Acceder a la documentación Swagger generada automáticamente en:
    ```bash
    http://127.0.0.1:8000/docs
    ```
    ![Ejemplo de Documentacion](https://i.ibb.co/xt7BKHwL/Docs-Swagger.png)

## Pruebas Unitarias
- Usamos pytest para ejecutar las pruebas.
1. Asegúrate de que la BD de pruebas está configurada correctamente.
2. Ejecuta:
    ```bash
    pytest
    ```
3. Verás un resumen de los tests ejecutados y si pasaron o fallaron.
    ![Ejemplo de Unit Test](https://i.ibb.co/k25ZRdb9/UnitTest.png)

## Pruebas de Carga con JMeter
1. Instalar `JMeter` (descargar binario desde la [Página Oficial](https://jmeter.apache.org/download_jmeter.cgi)).
2. `Crear un plan de prueba` (Test Plan) para simular usuarios concurrentes:
    - Agregar un `Thread Group` (cantidad de threads, ramp-up, etc.).
    - Agregar `Samplers` HTTP Request a /usuarios/, /usuarios/{id}, etc.
    - Configurar `CSV Data Set Config` o funciones `JMeter` para datos dinámicos.
1. `Ejecutar` y analizar
    - Métricas de latencia, throughput, error %, etc.
    - Ajustar tu API o infraestructura según los hallazgos.

    ![Ejemplo de Jmeter](https://i.ibb.co/HpFCjnmM/Jmeter.png)

## Buenas practicas en la nomenclatura de carpetas y archivos

### Carpetas
- **Kebab-case NO es recomendado** en carpetas (no es compatible con `import` en Python). 
- Para nombrar carpetas usar **snake_case** (letras minúsculas con guion bajo).
- Se usa inglés para nombrar las carpetas de la estructura del proyecto.
- Se deben incluir archivos **__init__.py** en carpetas que son paquetes Python.

| Tipo de Carpeta | Convención | Ejemplo |
|----------------|------------|---------|
| **Módulos**   | `snake_case` | `gestion_usuarios/`, `reporte_ventas/` |
| **Servicios** | `snake_case` | `usuario_service.py`, `producto_service.py` |
| **Modelos**   | `PascalCase` | `Usuario.py`, `Producto.py` |
| **Tests**     | `snake_case` | `test_usuario.py`, `test_producto.py` |



Ejemplos de carpetas
- **Si representa una acción, el verbo debe ir al inicio** (`listar_usuarios`). 

```sh
features/
 ├── listar_usuarios/
 │   ├── controllers/
 │   │   ├── listar_usuarios_controller.py
```

- **Si el módulo representa una entidad (nombre descriptivo)**
```sh
features/
 ├── gestion_productos/
 │   ├── controllers/
 │   │   ├── producto_controller.py
 │   ├── services/
 │   │   ├── producto_service.py
 │   ├── models/
 │   │   ├── Producto.py
```
### Archivos
- Se que recomienda el uso de snake_case (letras minúsculas con guiones bajos).
- Se usa español para nombrar los Archivos.
- Usar el sufijo respectivo ( .service.py, .routes.py, .controller.py ).

Ejemplos de archivos
- **Si representa una acción, el verbo debe ir al inicio** (`listar_usuarios.py`). 

```sh
features/
 ├── listar_usuarios/
 │   ├── controllers/
 │   │   ├── listar_usuarios_controller.py
```

| Tipo de archivo     | Convención recomendada  | Ejemplo |
|---------------------|------------------------|---------|
| **Módulos (archivos .py)** | `snake_case.py` | `usuario_service.py` |
| **Modelos** | `snake_case.py` | `usuario.py`, `orden.py` |
| **Esquemas (Schemas Pydantic)** | `snake_case.py` | `usuario_schema.py` |
| **Rutas (FastAPI)** | `snake_case.py` | `usuario_routes.py` |
| **Controladores** | `snake_case.py` | `autorizar_controller.py` |
| **Servicios (Lógica de negocio)** | `snake_case.py` | `pago_service.py` |
| **Middlewares** | `snake_case.py` | `autorizar_middleware.py` |
| **Utilidades (Helpers)** | `snake_case.py` | `email_utils.py` |
| **Configuración** | `snake_case.py` | `config.py`, `settings.py` |
| **Archivos de Pruebas** | `test_snake_case.py` | `test_user.py` |
| **Archivos especiales** | (`__init__.py`, `main.py`) | `__init__.py`, `main.py` |

**⚠️ Nota importante:** En **Python**, los archivos con `kebab-case` (`user-service.py`) pueden generar errores al importar módulos, por lo que **se debe usar `snake_case`**.