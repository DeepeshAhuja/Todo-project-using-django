# Todo-project-using-django
A simple Todo project

## Steps to run the project
1. Install Django: 
    - Run `pip install django` to install Django.

2. Create a virtual environment:
    - Run `python -m venv env` to create a virtual environment.
    - Activate the virtual environment using the appropriate command for your operating system.

3. Create a project:
    - Run `django-admin startproject project_name` to create a new Django project.

4. Create an app:
    - Run `python manage.py startapp app_name` to create a new Django app.

5. Create a model:
    - Define your model classes in the `models.py` file of your app.

6. Migrate the database:
    - Run `python manage.py makemigrations` to create the necessary database migrations.
    - Run `python manage.py migrate` to apply the migrations and create the database tables.

7. Run the server:
    - Run `python manage.py runserver` to start the development server.