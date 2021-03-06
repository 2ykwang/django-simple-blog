# Generated by Django 4.0.5 on 2022-06-12 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20220611_1538'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-published'], 'verbose_name': '게시글', 'verbose_name_plural': '게시글'},
        ),
        migrations.AddField(
            model_name='post',
            name='use_comment',
            field=models.BooleanField(default=True, verbose_name='댓글 허용'),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to='posts.category', verbose_name='카테고리'),
        ),
        migrations.AlterField(
            model_name='post',
            name='is_page',
            field=models.BooleanField(default=False, help_text='페이지 여부를 체크합니다. 페이지는 카테고리에 노출되지 않습니다.', verbose_name='페이지'),
        ),
    ]
