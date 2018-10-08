import os
from service_evaluation.settings.base import *


DEBUG = False
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'HOST': os.environ['DB_SERVICE'],
        'PORT': os.environ['DB_PORT']
    }
}

MEDIA_ROOT = os.environ.get('MEDIA_ROOT', os.path.join('/', 'var', 'www', 'scieval', 'media'))
STATIC_ROOT = os.environ.get('STATIC_ROOT', os.path.join('/', 'var', 'www', 'scieval', 'static'))
