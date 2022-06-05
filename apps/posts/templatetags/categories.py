from django import template

from apps.posts.models import Category

register = template.Library()


@register.inclusion_tag("posts/categories.html")
def show_categories():
    categories = Category.objects.with_post_counts().only("name", "slug").all()
    return {"categories": categories}
