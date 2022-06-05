from django.db import models

from apps.posts.models import Post


class Menu(models.Model):
    class Meta:
        verbose_name = "메뉴"
        verbose_name_plural = "메뉴"
        ordering = ["order"]

    name = models.CharField(verbose_name="메뉴 이름", max_length=30)
    description = models.CharField(verbose_name="설명", max_length=30)

    link = models.URLField(verbose_name="연결 할 주소", null=True, blank=True)
    post = models.ForeignKey(
        to=Post,
        verbose_name="연결 할 포스트",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    order = models.SmallIntegerField(verbose_name="순서", default=0)

    def __str__(self):
        return self.name

    def get_target_url(self) -> str:
        if self.link:
            return self.link
        if self.post:
            return self.post.get_absolute_url()
        raise ValueError("link 또는 post 값이 필요합니다.")
