from pathlib import Path
import os
import dj_database_url

# -----------------------------
# BASE
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# -----------------------------
# SECURITY
# -----------------------------
SECRET_KEY = os.environ.get('DJ_SECRET_KEY', 'troque-esta-chave-por-uma-secreta')
DEBUG = os.environ.get('DJ_DEBUG', 'False') == 'True'
ALLOWED_HOSTS = ['*']  # você pode trocar por ['seu-dominio.com'] depois

# -----------------------------
# APPS
# -----------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'portfolio',
    'crispy_forms',
]

# -----------------------------
# MIDDLEWARE
# -----------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # serve static files
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

# -----------------------------
# URLS & TEMPLATES
# -----------------------------
ROOT_URLCONF = 'site_demo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'portfolio' / 'templates'],
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

WSGI_APPLICATION = 'site_demo.wsgi.application'

# -----------------------------
# DATABASE
# -----------------------------
DATABASE_URL = os.environ.get(
    'DATABASE_URL',
    'postgresql://usuario:senha@host:5432/banco'
)

DATABASES = {
    'default': dj_database_url.parse(DATABASE_URL, conn_max_age=600)
}

# Força SSL para PostgreSQL no Render
DATABASES['default']['OPTIONS'] = {'sslmode': 'require'}

# -----------------------------
# STATIC & MEDIA
# -----------------------------
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# WhiteNoise
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# -----------------------------
# EMAIL (DEV)
# -----------------------------
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# -----------------------------
# SECURITY PROXY
# -----------------------------
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
