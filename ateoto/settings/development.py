from ateoto.settings.base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'testing.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
     }
}

AWS_S3_CUSTOM_DOMAIN = 'dev-static.ateoto.com'
AWS_STORAGE_BUCKET_NAME = SECRETS['aws_storage_dev_bucket_name']

try:
    from local_settings import *
except:
    pass
