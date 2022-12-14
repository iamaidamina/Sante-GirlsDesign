# Santé

This web app allows a homecare company to manage information relative to its care services, as well as gives remote access to clinical reports (they are permanently updated by medical staff) to patients and relatives.  

## Table of Contents

1. [Development Team](#development-team)
2. [Tech Stack](#tech-stack)
3. [Database](#)
4. [Mockups](#)
5. [Instruciones para correr el projecto localmente](#)
6. [Comando para servir el app](#)

## Development Team
- Laura Barreto
- Laura Olivares
- Aida Mina
- Johanna Mora F

## Tech Stack
- Data Layer
  - PostgreSQL
  - Heroku
  - TablePlus

# Instruciones para correr el projecto localmente
- Para correr el projecto localmente es necesario crear el entorno de python ( env ).
- - Correr el comando 'python -m venv env' desde el folder 'sante-be'.

- Luego proceda a activar el servidor ejecutando:
- - source env/bin/activate para mac
- -  env/bin/activate para windows

- Posteriormente se debe instalar django, django rest-framework, jwt y psycopg2 corriendo los siuientes comandos: 
- - pip install django 
- - pip install djangorestframework
- - pip install psycopg2
- - pip install djangorestframework-simplejwt

# Comando para servir el app
- python manage.py runserver
- Se ejecutará el servidor localmente en la dirección http://127.0.0.1:8000/