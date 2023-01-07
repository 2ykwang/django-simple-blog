# https://github.com/Suor/django-cacheops
from config.settings.utils import get_value

CACHEOPS_REDIS = {
    "host": get_value("REDIS_HOST"),  # redis-server is on same machine
    "port": int(get_value("REDIS_PORT", default="6379")),  # default redis port
    "db": 1,  # SELECT non-default redis database
}
CACHEOPS_DEFAULTS = {"timeout": 60 * 3}
# 'all' is an alias for {'get', 'fetch', 'count', 'aggregate', 'exists'}
CACHEOPS = {
    "auth.user": {"ops": "get", "timeout": 60 * 15},
    "posts.post": {"ops": {"fetch"}, "timeout": 60},
    "posts.category": {"ops": {"fetch"}, "timeout": 60},
    "main.link": {"ops": {"fetch"}, "timeout": 60},
}
