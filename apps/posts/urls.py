from django.urls import path

from .apps import PostsConfig as Config
from .views import PostDetailView, PostListView

app_name = Config.name

urlpatterns = [
    path("posts/<slug>", PostDetailView.as_view(), name="post_detail"),
    path("posts/", PostListView.as_view(), name="post_list"),
]
