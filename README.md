# TP Programación 4 — Backend Parte 1 (FastAPI)

API construida con **FastAPI** y **Pydantic** siguiendo la estructura del proyecto (`models/`, `routers/` y `main.py`).

## Instalación de dependencias

1. Crear y activar el entorno virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Instalar las dependencias:

```bash
pip install -r requirements.txt
```

*(O instalar directamente FastAPI con `pip install "fastapi[standard]"`).*

## Levantar la aplicación

Con el entorno virtual activado, ejecutar en modo desarrollo:

```bash
fastapi dev main.py
```

- **API:** `http://127.0.0.1:8000`
- **Documentación interactiva (Swagger):** `http://127.0.0.1:8000/docs`
