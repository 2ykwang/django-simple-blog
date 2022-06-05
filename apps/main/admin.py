from django.contrib import admin

from .models import Link


class LinkAdmin(admin.ModelAdmin):

    list_display = [
        "name",
        "description",
        "get_target_url",
        "order",
    ]
    fields = [
        "name",
        "description",
        "link",
        "post",
        "get_target_url",
        "is_open_new_window",
        "order",
    ]
    readonly_fields = ["get_target_url"]

    def get_target_url(self, link: Link) -> str:
        return link.get_target_url()

    get_target_url.short_description = "연결된 URL"


admin.site.register(Link, LinkAdmin)
