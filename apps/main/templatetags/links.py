from django import template

from apps.main.models import Link

register = template.Library()


@register.inclusion_tag("main/link.html")
def show_links():
    links = (
        Link.objects.select_related("post")
        .only("name", "link", "post__slug", "is_open_new_window")
        .all()
    )
    return {"links": links}
