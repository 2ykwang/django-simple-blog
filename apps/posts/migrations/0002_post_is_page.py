# Generated by Django 4.0.5 on 2022-06-06 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_page',
            field=models.BooleanField(default=False, verbose_name='페이지'),
        ),
    ]
