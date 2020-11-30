import os
from app.settings.base import *


ALLOWED_HOSTS = ['*']

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

CORS_ORIGIN_WHITELIST = (
    'http://localhost:8000',
    'http://localhost:3000',
    # 'https://nightly.grad4-api.com'
)

CORS_ALLOWED_ORIGINS = [
    'http://localhost:8000',
    '127.0.0.1:3000',
    'http://localhost:3000',
    # 'https://nightly.grad4-api.com'
]

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]
CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

DEBUG = True

FRONTEND_URL = "http://localhost:3000/"


STATIC_URL = '/static/'


AUTH_USER_MODEL = 'core.User'  # core is the name of app and User is the model


SITE_URL = 'http://localhost:3000'
