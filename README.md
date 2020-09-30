# Django Project: Local Library

## Logins for App
````
username: user1                 |         username: librarian1                    
password: user1password         |         password: user1password
````
## Setting up a Django development environment

### Using Django inside a Python virtual environment
- ``sudo pip3 install virtualenvwrapper``
- Then add the following lines of code to your shell startup file .bashrc
````
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export VIRTUALENVWRAPPER_VIRTUALENV_ARGS=' -p /usr/bin/python3 '
export PROJECT_HOME=$HOME/Devel``
source /usr/local/bin/virtualenvwrapper.sh
````
- Then reload the startup file: ``source ~/.bashrc``

### Using the virtual environment
- ``deactivate`` — Exit out of the current Python virtual environment
- ``workon`` — List available virtual environments
- ``workon <name_of_environment>`` — Activate the specified Python virtual environment
- ``rmvirtualenv <name_of_environment>`` — Remove the specified environment.

## Creating a skeleton website

### Creating a new project
-  Create the new project using the ``django-admin startproject`` command
    - ``django-admin startproject <new_project_name>``
- The ``manage.py`` script is used to create applications, work with databases, and start the development web server. 
-  ``__init__.py`` is an empty file that instructs Python to treat this directory as a Python package.
- ``settings.py`` contains all the website settings, including registering any applications we create, the location of our static files, database configuration details, etc.  
- ``urls.py`` defines the site URL-to-view mappings. While this could contain all the URL mapping code, it is more common to delegate some of the mappings to particular applications, as you'll see later.
- ``wsgi.py`` is used to help your Django application communicate with the webserver. You can treat this as boilerplate.
- ``asgi.py`` is a standard for Python asynchronous web apps and servers to communicate with each other. ASGI is the asynchronous successor to WSGI and provides a standard for both asynchronous and synchronous Python apps (whereas WSGI provided a standard for synchronous apps only). It is backward-compatible with WSGI and supports multiple servers and application frameworks.

### Creating an application
- ``python3 manage.py startapp <new_app_name>``
    - A ``migrations`` folder, used to store "migrations" — files that allow you to automatically update your database as you modify your models. 
    - ``_init__.py`` — an empty file created here so that Django/Python will recognize the folder as a Python Package and allow you to use its objects within other parts of the project.

#### Registering the new application
- Open the project settings file, ``django_projects/locallibrary/locallibrary/settings.py``, and find the definition for the INSTALLED_APPS list. Then add a new line at the end of the list:
```` 
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    '<new_app_name>', 
]
````

## Testing the website framework

###  Running database migrations 
- Django uses an Object-Relational-Mapper (ORM) to map model definitions in the Django code to the data structure used by the underlying database. As we change our model definitions, Django tracks the changes and can create database migration scripts (in /locallibrary/catalog/migrations/) to automatically migrate the underlying data structure in the database to match the model.
- Run the following commands to define tables for those models in the database:
````
python3 manage.py makemigrations
python3 manage.py migrate
````

### Running the website
- Run the development web server by calling the ``runserver`` command:
- ``python3 manage.py runserver``

## Django Admin Site

### Registering Models
- Open admin.py
- Then import the models and call ``admin.site.register`` to register the models:
````
from .models import Author, Genre, Book, BookInstance

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(BookInstance)

````

### Creating a superuser
``python3 manage.py createsuperuser``

## Testing a Django Web Application

The easiest way to run all the tests is to use the command:
``python3 manage.py test``
- This will discover all files named with the pattern test*.py under the current directory and run all tests defined using appropriate base classes
 <br>
 
 - If you get errors similar to: ``ValueError: Missing staticfiles manifest entry ...`` this may be because testing does not run collectstatic by default and your app is using a storage class that requires it 
 - There are a number of ways you can overcome this problem - the easiest is to simply run collectstatic before running the tests:
 - ``python3 manage.py collectstatic``

 ### Showing more test information
 - ``python3 manage.py test --verbosity=2``
 - The allowed verbosity levels are 0, 1, 2, and 3, with the default being "1".

 ### Running a Specific test
 - ``python3 manage.py test catalog.tests.test_models.YourTestClass``

 ## Requirements
 ``pip3 freeze > requirements.txt``