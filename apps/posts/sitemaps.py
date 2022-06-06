from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import Category, Post


class PostSitemap(Sitemap):
    changefreq = "daily"
    languages = ["ko_KR"]
    priority = 0.7

    def items(self):
        return Post.published_posts.filter(status__in=Post.public_on_category_status())

    def lastmod(self, post: Post):
        return post.updated


class PageSitemap(Sitemap):
    changefreq = "daily"
    languages = ["ko_KR"]
    priority = 0.7

    def items(self):
        return Post.pages.all()

    def lastmod(self, post: Post):
        return post.updated


class CategorySitemap(Sitemap):
    changefreq = "weekly"
    languages = ["ko_KR"]
    priority = 0.5

    def items(self):
        return Category.objects.all()


class PostsStaticSitemap(Sitemap):
    changefreq = "never"
    languages = ["ko_KR"]
    priority = 0.3

    def items(self):
        return ["apps.posts:post_list"]

    def location(self, item):
        return reverse(item)
