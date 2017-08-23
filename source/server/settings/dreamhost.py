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
