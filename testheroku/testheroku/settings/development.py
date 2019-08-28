import os
from .common import *
from decouple import config

# ############## DEBUG
DEBUG = config('DEBUG_DESENV', default=True, cast=bool)

# ############## Servidores autorizados
ALLOWED_HOSTS = config('ALLOWED_HOSTS_DEV', cast=lambda v: [s.strip() for s in v.split(',')])

# #Apps Instalados
# INSTALLED_APPS += [
# 
# ]

# ############## MIDDLEWARE

# Template

# DATABASES Postgre
DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': config('DB_NAME'),
            'USER': config('DB_USER'),
            'PASSWORD': config('DB_PASSWORD'),
            'HOST': config('DB_HOST'),
            'PORT': config('DB_PORT', default=5432),
        }
    }

# ########################## Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'  # aponta para dentro de cada app core
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') # Heroku pode servir desde que seja nesta pasta
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )
