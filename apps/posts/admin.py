from django.contrib import admin
from django.db import models
from markdownx.widgets import AdminMarkdownxWidget

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "created"]
    fields = ["title", "content", "slug", "updated", "created"]
    readonly_fields = ["updated", "created"]
    formfield_overrides = {models.TextField: {"widget": AdminMarkdownxWidget}}


admin.site.register(Post, PostAdmin)
