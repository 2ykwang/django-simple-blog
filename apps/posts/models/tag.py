from django.db import models


class Tag(models.Model):
    name = models.CharField(verbose_name="이름", max_length=40)

    class Meta:
        verbose_name = "태그"
        verbose_name_plural = "태그"
