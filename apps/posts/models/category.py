from django.db import models
from django.db.models import Q
from django.db.models.functions import Coalesce
from django.urls import reverse

from apps.posts.apps import PostsConfig as Config


class CategoryManager(models.Manager):
    def with_post_counts(self):
        from apps.posts.models import Post

        return self.annotate(
            post_counts=Coalesce(
                models.Count(
                    "posts",
                    filter=Q(
                        posts__status__in=Post.public_on_category_status()
                    ),
                ),
                0,
            )
        )


class Category(models.Model):
    class Meta:
        verbose_name = "카테고리"
        verbose_name_plural = "카테고리"
        ordering = ["order"]

    name = models.CharField(verbose_name="이름", max_length=40, unique=True)
    slug = models.SlugField(
        verbose_name="슬러그", max_length=40, allow_unicode=True, unique=True
    )
    order = models.SmallIntegerField(verbose_name="카테고리 순서", default=0)
    objects = CategoryManager()

    def get_posts(self):
        return self.posts.public_on_category()

    def get_absolute_url(self):
        return reverse(
            f"{Config.name}:category_view", kwargs={"slug": self.slug}
        )

    def __str__(self) -> str:
        return self.name
