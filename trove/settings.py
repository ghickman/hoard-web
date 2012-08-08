# Django settings for trove project.
import os

import dj_database_url


DIRNAME = os.path.abspath(os.path.dirname(__file__))

DEBUG = bool(os.environ.get('DEBUG', False))

ADMINS = (('George Hickman', 'george@ghickman.co.uk'),)
MANAGERS = ADMINS

DATABASES = {
    'default': dj_database_url.config(default='postgres://localhost/trove')
}

TIME_ZONE = 'Europe/London'
USE_TZ = True

LANGUAGE_CODE = 'en-gb'
USE_I18N = True  # Internationalization
USE_L10N = True  # Locale

# S3 Backend
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

# Static
MEDIA_ROOT = 'client_media'
MEDIA_URL = '/media/'
STATIC_ROOT = 'static_media'
STATIC_URL = 'http://{0}.s3.amazonaws.com/'.format(AWS_STORAGE_BUCKET_NAME)
TEMPLATE_DIRS = (os.path.join(DIRNAME, 'templates'))

ROOT_URLCONF = 'trove.urls'
SECRET_KEY = 'pl#%lb5=ws784n%ioe@+1f*s_1**e#g4f225*pr0&hjll6kw%q'
SITE_ID = 1
WSGI_APPLICATION = 'trove.wsgi.application'

MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]
if not os.environ.get('SSL', True):
    MIDDLEWARE_CLASSES.insert(0, 'sslify.middleware.SSLifyMiddleware')

INSTALLED_APPS = (
    'trove',

    'admin_sso',
    'django_extensions',
    'djangorestframework',
    'raven.contrib.django',
    'storages',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
)

SENTRY_DSN = os.environ.get('SENTRY_DSN')
SENTRY_TEST = DEBUG
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

