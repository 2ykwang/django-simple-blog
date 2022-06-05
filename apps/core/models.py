from django.db import models


class TimeStampedModel(models.Model):

    created = models.DateTimeField(verbose_name="생성 일", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="수정 일", auto_now=True)

    class Meta:
        abstract = True
