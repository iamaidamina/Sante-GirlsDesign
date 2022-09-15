# Santé

This web app allows a homecare company to manage information relative to its care services, as well as gives remote access to clinical reports (they are permanently updated by medical staff) to patients and relatives.  

## Table of Contents

1. [Development Team](#development-team)
2. [Tech Stack](#tech-stack)
3. [Database](#)
4. [Mockups](#)

## Development Team
- Laura Barreto
- Laura Olivares
- Aida Mina

## Tech Stack
- Data Layer
  - PostgreSQL
  - Heroku
  - TablePlus

# Instruciones para correr el projecto localmente
- Para correr el projecto localmente es necesario crear el entorno de python ( env ).
- Para esto se debe correr el comando 'python -m venv env' desde el folder 'sante-be'.
- Posteriormente se debe instalar django y dejango rest framework corriendo el comando: "pip install django & pip install djangorestframework"

# Comando activar el servidor
- source env/bin/activate para mac
- env/bin/activate para windows

# Comando para servir el app
- python manage.py runserver
- Se ejecutará el servidor localmente en la dirección http://127.0.0.1:8000/
