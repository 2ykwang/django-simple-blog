from django.contrib import admin
from django.db import models
from markdownx.widgets import AdminMarkdownxWidget

from .models import Category, Post


class PostAdmin(admin.ModelAdmin):
    search_fields = ("title", "content")
    list_select_related = ("category",)
    list_display = (
        "title",
        "category",
        "slug",
        "is_page",
        "published",
        "updated",
    )

    fieldsets = (
        (
            "게글",
            {
                "fields": ("title", "content"),
                "classes": ("wide", "extrapretty"),
            },
        ),
        (
            "게시글 정보",
            {
                "fields": ("description", "thumbnail", "published"),
            },
        ),
        (
            "게시 옵션",
            {
                "fields": (
                    "slug",
                    "status",
                    "category",
                    "is_page",
                    "use_comment",
                ),
            },
        ),
        (
            "날짜",
            {
                "fields": ("created", "updated"),
            },
        ),
    )

    readonly_fields = ("updated", "created")
    formfield_overrides = {models.TextField: {"widget": AdminMarkdownxWidget}}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "order")
    fields = ("name", "slug", "order")


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
