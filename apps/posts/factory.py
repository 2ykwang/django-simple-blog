import factory.fuzzy
from factory.django import DjangoModelFactory

from apps.posts.models import Category, Post


class CategoryFactory(DjangoModelFactory):

    name = factory.sequence(lambda n: f"카테고리 ({n})")
    slug = factory.Faker("slug")
    order = factory.sequence(lambda n: n)

    class Meta:
        model = Category
        django_get_or_create = ("name",)


class PostFactory(DjangoModelFactory):

    title = factory.Faker("sentence")
    slug = factory.Faker("slug")
    content = factory.Faker("paragraph", nb_sentences=30)
    description = factory.lazy_attribute(lambda obj: obj.content[:140])
    status = factory.fuzzy.FuzzyChoice(Post.Status)
    is_page = False
    category = factory.SubFactory(CategoryFactory)
    thumbnail = factory.django.ImageField(color="red")

    class Meta:
        model = Post
        django_get_or_create = ("slug",)
