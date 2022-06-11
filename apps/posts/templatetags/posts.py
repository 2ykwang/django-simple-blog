from django import template

from apps.posts.models import Post

register = template.Library()


@register.inclusion_tag("posts/recent_posts.html")
def show_recent_posts():
    posts = Post.published_posts.all()[:5]
    return {"posts": posts}
