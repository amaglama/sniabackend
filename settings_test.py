from .settings import *  # Importa todas las configuraciones existentes

# Sobrescribe la configuración de la base de datos para usar SQLite en memoria
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

# Opcional: Configuraciones adicionales para pruebas
INSTALLED_APPS += [
    'rest_framework',
    'pytest_django',
    # Añade otras aplicaciones necesarias
]

# Configuraciones de REST Framework para pruebas
REST_FRAMEWORK = {
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
    # Otras configuraciones según tus necesidades
}
