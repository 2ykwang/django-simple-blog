from config.settings.base import *

DEBUG = True

INTERNAL_IPS = [
    "127.0.0.1",
]
try:
    ALLOWED_HOSTS = [x.strip() for x in get_value("ALLOWED_HOSTS").split(",")]
except KeyError:
    ALLOWED_HOSTS = ["localhost", "127.0.0.1", "0.0.0.0"]

if ENABLE_DEBUG_TOOLBAR:
    INSTALLED_APPS += ["debug_toolbar"]
    MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]
