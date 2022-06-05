from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView, TemplateView, View

from .models import Category, Post


class PostDetailView(DetailView):
    model = Post


class PostListView(ListView):
    def get_queryset(self):
        queryset = Post.objects.select_related("category")
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context


class CategoryPostListView(ListView):
    template_name = "posts/post_list.html"

    def get_queryset(self):
        category = get_object_or_404(Category, slug=self.kwargs.get("slug"))
        return category.get_posts()
