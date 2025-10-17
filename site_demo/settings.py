from pathlib import Path
import os
import dj_database_url

# ---------------------------------------------
# BASE DIR
# ---------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# ---------------------------------------------
# SECRET KEY & DEBUG
# ---------------------------------------------
SECRET_KEY = os.environ.get('DJ_SECRET_KEY', 'troque-esta-chave-por-uma-secreta')
DEBUG = os.environ.get('DJ_DEBUG', 'False') == 'True'

# ---------------------------------------------
# ALLOWED HOSTS
# ---------------------------------------------
ALLOWED_HOSTS = ['*']  # Em produção, especifique seu domínio

# ---------------------------------------------
# INSTALLED APPS
# ---------------------------------------------
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

# ---------------------------------------------
# MIDDLEWARE
# ---------------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Serve static files
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

# ---------------------------------------------
# ROOT URLCONF
# ---------------------------------------------
ROOT_URLCONF = 'site_demo.urls'

# ---------------------------------------------
# TEMPLATES
# ---------------------------------------------
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

# ---------------------------------------------
# WSGI
# ---------------------------------------------
WSGI_APPLICATION = 'site_demo.wsgi.application'

# ---------------------------------------------
# DATABASE
# ---------------------------------------------
DATABASES = {
    'default': dj_database_url.parse(
        os.environ.get(
            'DATABASE_URL',
            'postgres://wesley_portfolio:tqiwTKN8ro7Hx9tMLAQhI00Hulq8IdgY@dpg-d3oq07pr0fns73doui1g-a.oregon-postgres.render.com:5432/wesley_portfolio_db'
        ),
        conn_max_age=600,
        ssl_require=True  # garante SSL no Render
    )
}

# ---------------------------------------------
# STATIC & MEDIA
# ---------------------------------------------
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# WhiteNoise: otimiza entrega de arquivos estáticos
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# ---------------------------------------------
# EMAIL (desenvolvimento)
# ---------------------------------------------
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# ---------------------------------------------
# SSL e Proxy
# ---------------------------------------------
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# ---------------------------------------------
# Django Crispy Forms
# ---------------------------------------------
CRISPY_TEMPLATE_PACK = 'bootstrap4'
