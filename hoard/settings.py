# Django settings for hoard project.
import os

import django_cache_url
import dj_database_url


DIRNAME = os.path.abspath(os.path.dirname(__file__))

DEBUG = bool(os.environ.get('DEBUG', False))

ADMINS = (('George Hickman', 'george@ghickman.co.uk'),)
MANAGERS = ADMINS

DATABASES = {
    'default': dj_database_url.config(default='postgres://localhost/hoard')
}
CACHES = {'default': django_cache_url.config('django_pylibmc://')}

TIME_ZONE = 'Europe/London'
USE_TZ = True

LANGUAGE_CODE = 'en-gb'
USE_I18N = True  # Internationalization
USE_L10N = True  # Locale

# S3 Backend
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_AUTH = False
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
STATICFILES_STORAGE = os.environ.get('STATICFILES_STORAGE', 'storages.backends.s3boto.S3BotoStorage')
S3_URL = 'http://{0}.s3.amazonaws.com/'.format(AWS_STORAGE_BUCKET_NAME)

# Static
MEDIA_ROOT = 'client_media'
MEDIA_URL = '/media/'
STATIC_ROOT = 'static_media'
STATIC_URL = os.environ.get('STATIC_URL', S3_URL)
TEMPLATE_DIRS = (os.path.join(DIRNAME, 'templates'))

ROOT_URLCONF = 'hoard.urls'
SECRET_KEY = 'pl#%lb5=ws784n%ioe@+1f*s_1**e#g4f225*pr0&hjll6kw%q'
SITE_ID = 1
WSGI_APPLICATION = 'hoard.wsgi.application'

MIDDLEWARE_CLASSES = (
    'sslify.middleware.SSLifyMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

INSTALLED_APPS = (
    'hoard',

    'admin_sso',
    'django_extensions',
    'raven.contrib.django',
    'rest_framework',
    'rest_framework.authtoken',
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
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
         'console': {
             'format': '[%(asctime)s][%(levelname)s] %(name)s %(filename)s:%(funcName)s:%(lineno)d | %(message)s',
             'datefmt': '%H:%M:%S',
         },
     },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'sentry': {
            'level': 'DEBUG',
            'filters': ['require_debug_false'],
            'class': 'raven.contrib.django.handlers.SentryHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'console',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['sentry', 'console'],
            'level': 'ERROR',
            'propagate': True,
        },
        'sentry.errors': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propogate': True,
        },
    }
}

# Rest Framework
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    )
}

