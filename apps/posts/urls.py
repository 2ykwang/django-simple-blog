from django.urls import path

from .apps import PostsConfig as Config
from .views import (
    CategoryPostListView,
    PageDetailView,
    PostDetailView,
    PostListView,
)

app_name = Config.name


post_urlpatterns = [
    path("pages/<slug>/", PageDetailView.as_view(), name="page_detail"),
    path("posts/<slug>/", PostDetailView.as_view(), name="post_detail"),
    path("posts/", PostListView.as_view(), name="post_list"),
]
category_urlpatterns = [
    path(
        "category/<slug>/", CategoryPostListView.as_view(), name="category_view"
    ),
]

urlpatterns = post_urlpatterns + category_urlpatterns
