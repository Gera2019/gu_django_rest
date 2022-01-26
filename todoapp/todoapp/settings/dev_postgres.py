from .dev import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'todo',
        'USER': 'dante',
        'PASSWORD': 'dante123456',
        'HOST': '192.168.1.80',
        'PORT': '5432',
    }
}