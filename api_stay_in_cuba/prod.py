from .base import *

# Override base.py settings here
DEBUG = False
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'stay'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'concordia',
        'USER': 'postgres',
        'PASSWORD': 'root*2019',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
