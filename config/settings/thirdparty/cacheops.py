# https://github.com/Suor/django-cacheops

CACHEOPS_REDIS = {
    "host": "localhost",  # redis-server is on same machine
    "port": 6379,  # default redis port
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
