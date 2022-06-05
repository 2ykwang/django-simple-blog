 from django import template

from apps.main.models import Menu

register = template.Library()


@register.inclusion_tag("main/menu.html")
def show_menus():
    menus = Menu.objects.all()
    # TODO: 카테고리 표시
    return {"menus": menus}
