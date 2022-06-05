from django.contrib import admin

from .models import Menu


class MenuAdmin(admin.ModelAdmin):

    list_display = ["name", "description", "get_target_url"]
    fields = ["name", "description", "link", "post", "get_target_url"]
    readonly_fields = ["get_target_url"]

    def get_target_url(self, menu: Menu) -> str:
        return menu.get_target_url()

    get_target_url.short_description = "연결된 URL"


admin.site.register(Menu, MenuAdmin)
