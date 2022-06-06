from typing import Any, Dict

from django.conf import settings


def analytics_gtag_id(request) -> Dict[str, Any]:
    return {"analytics_gtag_id": settings.ANALYTICS_GTAG_ID}
