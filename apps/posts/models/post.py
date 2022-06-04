from django.db import models


class Post(models.Model):
    class PostStatus(models.IntegerChoices):
        PUBLISHED = 0, "공개"
        DRAFT = 1, "초안"
        PRIVATE = 2, "비공개"

    title = models.CharField(verbose_name="제목", max_length=120)
    content = models.TextField(verbose_name="내용")

    slug = models.SlugField(verbose_name="슬러그")
    description = models.CharField(
        verbose_name="설명", max_length=140, null=True, blank=True
    )
    status = models.SmallIntegerField(
        verbose_name="상태", choices=PostStatus.choices, default=PostStatus.DRAFT
    )

    class Meta:
        verbose_name = "게시글"
        verbose_name_plural = "게시글"
