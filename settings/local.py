from common import *
from settings.secrets import DATABASE_PASSWORD

DEBUG = True
DEV_SERVER = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "1c936be3-d0b6-4ff3-98e7-e52ab714bde2ee41d22c-3619-4b7f-af3a-2f183bbaa80c6f82985a-0a5e-426d-923c-05e10625ecfc"
NEVERCACHE_KEY = "bf7791a4-d240-4683-94ec-b7fdc1afdadc090c124d-d74b-431e-8942-f73be6b4e68f52a01723-d009-43e1-a70a-36bb48ce671f"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
         "NAME": "dev.db",
         "USER": "",
         "PASSWORD": "",
         "HOST": "",
         "PORT": "",
    }
}

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql_psycopg2",
#          "NAME": "kayemyles_db",
#          "USER": "kayemyles",
#          "PASSWORD": DATABASE_PASSWORD,
#          "HOST": "localhost",
#          "PORT": "4444",
#     }
# }


try:
    from mezzanine.utils.conf import set_dynamic_settings
except ImportError:
    pass
else:
    set_dynamic_settings(globals())