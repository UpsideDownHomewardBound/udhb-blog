from settings.secrets import *
from common import *

DEBUG = True
DEV_SERVER = True

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
