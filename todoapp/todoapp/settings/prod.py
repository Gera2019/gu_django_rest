from .base import *

DEBUG = False
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'todo',
        'USER': 'dante',
        'PASSWORD': 'dante123456',
        'HOST': 'db',
        'PORT': '5432',
    }
}