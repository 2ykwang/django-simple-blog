from config.settings.base import *

DEBUG = False

ALLOWED_HOSTS = [x.strip() for x in get_value("ALLOWED_HOST").split(",")]
