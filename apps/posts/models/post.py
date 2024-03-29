from typing import Tuple

from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.html import strip_tags
from markdownx.utils import markdownify

from apps.core.fields import UUIDImageField
from apps.core.models import TimeStampedModel
from apps.posts.apps import PostsConfig as Config


class CustomPostQuerySet(models.QuerySet):
    def public_on_category(self):
        return self.filter(status__in=Post.public_on_category_status())

    def public(self):
        return self.filter(status__in=Post.public_status())


class PublishedManager(models.Manager):
    def get_queryset(self):
        return (
            super(PublishedManager, self).get_queryset().filter(is_page=False)
        )


class PageManager(models.Manager):
    def get_queryset(self):
        return super(PageManager, self).get_queryset().filter(is_page=True)


class Post(TimeStampedModel):
    class Status(models.IntegerChoices):
        PUBLISHED = 0, "공개"
        DRAFT = 1, "초안"
        PRIVATE = 2, "비공개"
        ONLY_LINK = 3, "일부 공개"

    class Meta:
        verbose_name = "게시글"
        verbose_name_plural = "게시글"
        ordering = ["-published"]

    objects = models.Manager.from_queryset(CustomPostQuerySet)()
    posts = PublishedManager.from_queryset(CustomPostQuerySet)()
    pages = PageManager.from_queryset(CustomPostQuerySet)()

    thumbnail = UUIDImageField(
        verbose_name="썸네일", upload_to="uploads/", null=True, blank=True
    )
    title = models.CharField(verbose_name="제목", max_length=120)
    content = models.TextField(verbose_name="내용")

    slug = models.SlugField(verbose_name="슬러그", allow_unicode=True, unique=True)
    description = models.CharField(
        verbose_name="설명", max_length=140, null=True, blank=True
    )
    status = models.SmallIntegerField(
        verbose_name="상태", choices=Status.choices, default=Status.DRAFT
    )
    is_page = models.BooleanField(
        verbose_name="페이지",
        default=False,
        help_text="페이지 여부를 체크합니다. 페이지는 카테고리에 노출되지 않습니다.",
    )
    category = models.ForeignKey(
        to="posts.category",
        related_name="posts",
        verbose_name="카테고리",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    published = models.DateTimeField(verbose_name="게시 일", default=timezone.now)

    use_comment = models.BooleanField(verbose_name="댓글 허용", default=True)

    def save(
        self,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None,
    ):
        if not self.description:
            # description을 빈 값으로 저장할 경우 내용에서 가져온다.
            # markdown - > html - > plain text 으로 변환 후 저장
            self.description = strip_tags(markdownify(self.content))[:140]

        super().save(force_insert, force_update, using, update_fields)

    @property
    def estimate_reading_time(self) -> int:
        wpm = 100
        word_count = len(self.content) // 5
        return word_count // wpm

    def get_absolute_url(self):
        if self.is_page:
            return reverse(
                f"{Config.name}:page_detail", kwargs={"slug": self.slug}
            )
        return reverse(f"{Config.name}:post_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

    @staticmethod
    def public_on_category_status() -> Tuple:
        return (Post.Status.PUBLISHED.value,)

    @staticmethod
    def public_status() -> Tuple:
        return Post.Status.PUBLISHED.value, Post.Status.ONLY_LINK.value
