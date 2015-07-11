from common import *

DEBUG = True
DEV_SERVER = False

GALLERY_GATHER_DELAY = 45

RAVEN_CONFIG = {
    'dsn': 'https://ba999676900348e896093777108be81a:fe3342e2b3aa499cb4a0ce52a5fb16bb@app.getsentry.com/44991',
}

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "kayemyles_db",
        "USER": "kayemyles",
        "PASSWORD": DATABASE_PASSWORD,
        "HOST": "localhost",
        "PORT": "5432",
    }
}

try:
    from mezzanine.utils.conf import set_dynamic_settings
except ImportError:
    pass
else:
    set_dynamic_settings(globals())

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,

    'formatters': {
        'console': {
            'format': '[%(asctime)s][%(levelname)s] %(name)s %(filename)s:%(funcName)s:%(lineno)d | %(message)s',
            'datefmt': '%H:%M:%S',
            },
        },

    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'console'
            },
        'sentry': {
            'level': 'ERROR',
            'class': 'raven.handlers.logging.SentryHandler',
            'dsn': 'https://ba999676900348e896093777108be81a:fe3342e2b3aa499cb4a0ce52a5fb16bb@app.getsentry.com/44991',
            },
        },

    'loggers': {
        '*': {
            'handlers': ['console', 'sentry'],
            'level': 'WARNING',
            'propagate': False,
            },
        'inventory': {
            'handlers': ['console', 'sentry'],
            'level': 'INFO',
            'propagate': True,
        },
        'the_comm_app': {
            'level': 'INFO',
            'propagate': True,
        },
    }
}