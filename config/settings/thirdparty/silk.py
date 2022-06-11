# https://github.com/jazzband/django-silk

SILKY_AUTHENTICATION = True  # User must login
SILKY_AUTHORISATION = True  # User must have permissions
LOGIN_REDIRECT_URL = "/"
LOGIN_URL = "/admin/login/"

SILKY_MAX_RESPONSE_BODY_SIZE = 1024  # If response body>1024kb, ignore
SILKY_INTERCEPT_PERCENT = 20  # 트래픽의 20%만 로깅
SILKY_MAX_RECORDED_REQUESTS = 10**4  # 레코드 개수 제한

SILKY_PYTHON_PROFILER = False
SILKY_ANALYZE_QUERIES = True
SILKY_META = True
