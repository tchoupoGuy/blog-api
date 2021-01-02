
import os
from enum import Enum

# Django-environ package
import environ
import datetime


class RuntimeEnvironment(Enum):
    DEV = 'app.settings.dev'
    NIGHTLY = 'settings.nightly'
    TESTING = 'settings.testing'
    STAGING = 'settings.staging'
    PROD = 'settings.prod'


IS_PROD = os.environ.get(
    'DJANGO_SETTINGS_MODULE') == RuntimeEnvironment.PROD.value
IS_STAGING = os.environ.get(
    'DJANGO_SETTINGS_MODULE') == RuntimeEnvironment.STAGING.value
IS_NIGHTLY = os.environ.get(
    'DJANGO_SETTINGS_MODULE') == RuntimeEnvironment.NIGHTLY.value

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

env = environ.Env()
env.read_env()

# reading the .<environment>.env file
try:
    if IS_PROD:
        env.read_env()
    elif IS_STAGING:
        env.read_env(env_file=os.path.join(BASE_DIR, "settings/.staging.env"))
    elif IS_NIGHTLY:
        env.read_env(env_file=os.path.join(BASE_DIR, "settings/.nightly.env"))
except:
    env.read_env()


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str(
    'SECRET_KEY', default='x%^y+vcv5jm@_s2p70(=(=x522*9+vqxcw2#05_tqz1ojd8)7e')
# SECRET_KEY = 'x%^y+vcv5jm@_s2p70(=(=x522*9+vqxcw2#05_tqz1ojd8)7e'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'core',
    'user',
    'tag',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DEBUG = True
# FRONTEND_URL = "http://localhost:3000/"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'


AUTH_USER_MODEL = 'core.User'  # core is the name of app and User is the model

FRONTEND_URL = "http://localhost:3000/"
