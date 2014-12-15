__author__ = 'peter'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Turn debugging off for production environments!
DEBUG = False

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
}

# Your uploaded files will be stored in <MEDIA_ROOT>/photologue/, so set it correctly!
MEDIA_ROOT = './media/'

MEDIA_URL = '/media/'
