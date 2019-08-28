import os
from .common import *
import dj_database_url
from decouple import config
# import django_heroku #VER2019081308-Precisa comentar para fazer as migrações no desenv, utilizar no mamage.py o ambiente de develop

# https://devcenter.heroku.com/articles/deploying-python
# https://devcenter.heroku.com/categories/working-with-django

# ############## DEBUG
DEBUG = config('DEBUG', default=False, cast=bool)

# ############## Servidores autorizados
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=lambda v: [s.strip() for s in v.split(',')])

# ############## DataBase - Heroku
# DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)
DATABASES = {'default': dj_database_url.config(conn_max_age=600, ssl_require=True)}
# DATABASE_URL = os.environ['DATABASE_URL']   #VER2019081308

# ########################## Static files (CSS, JavaScript, Images)
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'