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
python3 -m pip install 
- -  django 
- -  djangorestframework
- -  psycopg2
- -  djangorestframework-simplejwt
- -  django_heroku
- -  django-cors-headers

# Comando para servir el app
- python3 manage.py runserver
- Se ejecutará el servidor localmente en la dirección http://127.0.0.1:8000/

# Acertijos de las guias
1. Instalar django heroku localmente, la guia no lo menciona pero es necesario.
2. Seleccionar buildpack de heroku, la guia no lo menciona pero es necesario para poder desplegar.
    heroku buildpacks:set heroku/python
3. Subir a heroku solo carpeta-be, dado que heroku buscara el archivo manage.py en la raiz
4. Rama master tiene que existir, si se creo primero en github usar main. Si nunca se ha sincronizado con github usar master