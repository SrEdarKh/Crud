# Django CRM

Este es un sistema CRM (Customer Relationship Management) básico hecho con Django y Bootstrap. Permite:

- Registrar usuarios
- Iniciar sesión
- Mostrar registros en una tabla paginada
- CRUD de clientes o contactos

## Tecnologías

- Django 5
- Bootstrap 5
- Python 3.13
- SQLite

## Cómo correrlo localmente

```bash
git clone https://github.com/tu-usuario/Crud.git
cd Crud
python -m venv venv
source venv/bin/activate  # en Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py runserver
