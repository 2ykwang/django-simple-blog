from django import template
from django.utils.safestring import mark_safe
from markdownx.utils import markdownify

from apps.posts.models import Post

register = template.Library()


@register.inclusion_tag("posts/recent_posts.html")
def show_recent_posts():
    posts = Post.posts.public_on_category().all()[:5]
    return {"posts": posts}


@register.filter
def markdown(text: str):
    return mark_safe(markdownify(text))
