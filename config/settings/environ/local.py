from config.settings.base import *

DEBUG = True

INTERNAL_IPS = [
    "127.0.0.1",
]
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "0.0.0.0"]

if ENABLE_SILK:
    INSTALLED_APPS += ["silk"]
    MIDDLEWARE += ["silk.middleware.SilkyMiddleware"]

if ENABLE_DEBUG_TOOLBAR:
    INSTALLED_APPS += ["debug_toolbar"]
    MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]
