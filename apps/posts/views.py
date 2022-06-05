from django.views.generic import DetailView, ListView

from .models import Post


class PostDetailView(DetailView):
    model = Post


class PostListView(ListView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context
