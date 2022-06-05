from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):

    list_display = ["title", "created"]
    fields = ["title", "content", "slug", "updated", "created"]
    readonly_fields = ["updated", "created"]


admin.site.register(Post, PostAdmin)
