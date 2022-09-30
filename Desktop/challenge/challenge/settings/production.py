from .base import *
from decouple import config

DEBUG = True

ALLOWED_HOSTS = []

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.PyMemcacheCache',
        
        'LOCATION': '127.0.0.1:11211',
    }
}


