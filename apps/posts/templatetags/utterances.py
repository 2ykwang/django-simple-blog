from django import template
from django.conf import settings

register = template.Library()


@register.inclusion_tag("posts/utterances.html")
def utterances_comment():

    context = {
        "use_utterances_comment": settings.USE_UTTERANCES_COMMENT,
        "utterances_repo": settings.UTTERANCES_REPO,
        "utterances_label": settings.UTTERANCES_LABEL,
        "utterances_theme": settings.UTTERANCES_THEME,
        "utterances_issue_term": settings.UTTERANCES_ISSUE_TERM,
    }
    return context
