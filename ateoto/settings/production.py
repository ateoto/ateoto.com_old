from ateoto.settings.base import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': SECRETS['prod_db_name'],
        'USER': SECRETS['prod_db_user'],
        'PASSWORD': SECRETS['prod_db_pass'],
        'HOST': '',
        'PORT': '',
    }
}


try:
    from local_settings import *
except:
    pass
