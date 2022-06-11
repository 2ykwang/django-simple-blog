from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView, TemplateView, View

from .models import Category, Post


class PostDetailView(DetailView):
    model = Post

    def get_object(self, queryset=None):
        post = super(PostDetailView, self).get_object(queryset=queryset)

        if (
            not self.request.user.is_superuser
            and post.status not in Post.public_status()
        ):
            raise Http404()
        return post


class PostListView(ListView):
    def get_queryset(self):
        queryset = Post.published_posts.select_related("category").cache()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["list_title"] = "글 목록"
        return context


class CategoryPostListView(ListView):
    template_name = "posts/post_list.html"

    def _get_category(self):
        # TODO: select category 두 번 발생
        self.category = get_object_or_404(Category, slug=self.kwargs.get("slug"))
        return self.category

    def get_queryset(self):
        category = self._get_category()
        return category.get_posts()

    def get_context_data(self, *, object_list=None, **kwargs):
        category = self._get_category()
        context = super(CategoryPostListView, self).get_context_data()
        context["category"] = category
        context["list_title"] = f"{category.name} - 글 목록"
        return context
