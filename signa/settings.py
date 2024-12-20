import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = os.getenv('DEBUG') == 'True'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') 

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'corsheaders',
    
    'rest_framework',
    'brand'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # Debe ir antes de 'AuthenticationMiddleware'
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Debe ir después de 'SessionMiddleware'
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',  # Requerido para el admin
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
     'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DATABASE_NAME'),
        'USER': os.getenv('DATABASE_USER'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD'),
        'HOST': os.getenv('DATABASE_HOST'),
        'PORT': os.getenv('DATABASE_PORT'),
    }
}

ROOT_URLCONF = 'signa.urls'

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
}

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
]


CORS_ALLOW_ALL_ORIGINS = True

