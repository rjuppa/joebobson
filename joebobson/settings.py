"""
Django settings for joebobson project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3q5sdi^$tli*qc-%qh_#9_d*xo@_5yr)$4guqdzkko0eoc^t*l'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'grappelli',
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.contenttypes',
    'django_comments',
    'mptt',
    'tagging',
    'sorl.thumbnail',
    'tinymce',
    'zinnia_bootstrap',
    'zinnia',
    'zinnia_tinymce',
    'joeblog',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_LOADERS = [
    'app_namespace.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.eggs.Loader'
]

TEMPLATE_CONTEXT_PROCESSORS = (
  'django.contrib.auth.context_processors.auth',
  'django.core.context_processors.i18n',
  'django.core.context_processors.request',
  'zinnia.context_processors.version',  # Optional
)

ROOT_URLCONF = 'joebobson.urls'

WSGI_APPLICATION = 'joebobson.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
import dj_database_url

DATABASES = {
    'default': dj_database_url.config(),
    'default_old': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',     # '.postgresql_psycopg2', '.mysql', or '.oracle'
        'NAME': 'joeblog',   # Required to be non-empty string
        'USER': 'postgres',   # Required to be non-empty string
        'PASSWORD': 'xxxxxx',
        'HOST': '',     # Set to empty string for localhost.
        'PORT': '',     # Set to empty string for default.
        },
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/


STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"



ZINNIA_ENTRY_CONTENT_TEMPLATES = [
  ('zinnia/_short_entry_detail.html', 'Short entry template'),
]

ZINNIA_ENTRY_DETAIL_TEMPLATES = [
    ('zinnia/fullwidth_entry_detail.html', 'Fullwidth template'),
]

ZINNIA_PING_EXTERNAL_URLS = False
ZINNIA_SAVE_PING_DIRECTORIES = False
ZINNIA_PING_DIRECTORIES = ('http://ping.directory.com/',
                           'http://pong.directory.com/')

TINYMCE_JS_URL = os.path.join(MEDIA_URL, "js/tiny_mce/tiny_mce.js")




