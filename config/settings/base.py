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

USE_UTTERANCES_COMMENT = get_value("USE_UTTERANCES_COMMENT", default="0") == "1"
UTTERANCES_REPO = get_value("UTTERANCES_REPO", required=False)
UTTERANCES_ISSUE_TERM = get_value("UTTERANCES_ISSUE_TERM", default="pathname")
UTTERANCES_LABEL = get_value("UTTERANCES_LABEL", default="Comment")
UTTERANCES_THEME = get_value("UTTERANCES_THEME", default="github-light")
