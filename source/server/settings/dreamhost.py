from .base import *

STATIC_ROOT = '/home/fems/web/healthcheck.fe.fernandoe.com/public/static'

ALLOWED_HOSTS = ['healthcheck.fe.fernandoe.com', ]

from configparser import RawConfigParser
config = RawConfigParser()
config.read('/home/fems/conf/fe-healthcheck-server.ini')

DATABASES = {
    'default': {
        'ENGINE': config.get('database', 'DATABASE_ENGINE'),
        'NAME': config.get('database', 'DATABASE_NAME'),
        'USER': config.get('database', 'DATABASE_USER'),
        'PASSWORD': config.get('database', 'DATABASE_PASSWORD'),
        'HOST': config.get('database', 'DATABASE_HOST'),
        'PORT': config.get('database', 'DATABASE_PORT'),
        'OPTIONS': {
            'init_command': 'SET storage_engine=MyISAM',
        }
    }
}

EMAIL_HOST = config.get('email', 'EMAIL_HOST')
SERVER_EMAIL = config.get('email', 'SERVER_EMAIL')
EMAIL_HOST_USER = config.get('email', 'EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config.get('email', 'EMAIL_HOST_PASSWORD')
EMAIL_PORT = config.get('email', 'EMAIL_PORT')
EMAIL_USE_SSL = config.get('email', 'EMAIL_USE_SSL')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'verbose',
            'filename': config.get('logging', 'LOGGING_FILENAME'),
            'when': 'midnight',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        LOGGING_APPNAME: {
            'handlers': ['console', 'mail_admins', 'file'],
            'level': 'DEBUG'
        }
    }
}
