# Generated by Django 4.0.5 on 2022-06-06 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='링크 이름')),
                ('description', models.CharField(max_length=30, verbose_name='설명')),
                ('link', models.URLField(blank=True, null=True, verbose_name='연결 할 주소')),
                ('order', models.SmallIntegerField(default=0, verbose_name='순서')),
                ('is_open_new_window', models.BooleanField(default=False, verbose_name='새 창에서 열기')),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='posts.post', verbose_name='연결 할 포스트')),
            ],
            options={
                'verbose_name': '링크',
                'verbose_name_plural': '링크',
                'ordering': ['order'],
            },
        ),
    ]
