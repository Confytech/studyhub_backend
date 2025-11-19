import os
from pathlib import Path
from datetime import timedelta

# ----------------------------------
# BASE DIRECTORY
# ----------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# ----------------------------------
# SECURITY
# ----------------------------------
SECRET_KEY = 'django-insecure-your-secret-key'
DEBUG = True
ALLOWED_HOSTS = []

# ----------------------------------
# INSTALLED APPS
# ----------------------------------
INSTALLED_APPS = [
    # Django default apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party apps
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',

    # Local apps
    'apps.users',
    'apps.study',
    'apps.payments',
]

# ----------------------------------
# MIDDLEWARE
# ----------------------------------
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',   # CORS HEADER (Must be first)

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ----------------------------------
# CORS SETTINGS
# ----------------------------------
CORS_ALLOW_ALL_ORIGINS = True  # Allow all origins (React frontend friendly)

# ----------------------------------
# URL CONFIG
# ----------------------------------
ROOT_URLCONF = 'studyhub_backend_config.urls'

# ----------------------------------
# TEMPLATES
# ----------------------------------
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

# ----------------------------------
# WSGI / ASGI
# ----------------------------------
WSGI_APPLICATION = 'studyhub_backend_config.wsgi.application'
ASGI_APPLICATION = 'studyhub_backend_config.asgi.application'

# ----------------------------------
# DATABASE
# ----------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ----------------------------------
# PASSWORD VALIDATORS
# ----------------------------------
AUTH_PASSWORD_VALIDATORS = []

# ----------------------------------
# INTERNATIONALIZATION
# ----------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ----------------------------------
# STATIC FILES
# ----------------------------------
STATIC_URL = '/static/'

# ----------------------------------
# DEFAULT AUTO FIELD
# ----------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ----------------------------------
# CUSTOM USER MODEL
# ----------------------------------
AUTH_USER_MODEL = 'users.User'

# ----------------------------------
# DJANGO REST FRAMEWORK (DRF)
# ----------------------------------
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

# ----------------------------------
# SIMPLE JWT SETTINGS
# ----------------------------------
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': False,
    'AUTH_HEADER_TYPES': ('Bearer',),
}

