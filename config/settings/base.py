try:
    from dotenv import load_dotenv

    load_dotenv()
except ModuleNotFoundError:
    pass


from .django import *
from .thirdparty import *

# 값이 '1'일 경우 silk가 활성화 됩니다.
ENABLE_DEBUG_TOOLBAR = get_value("ENABLE_DEBUG_TOOLBAR", default="0") == "1"
ANALYTICS_GTAG_ID = get_value("ANALYTICS_GTAG_ID", required=False)
