from django.urls import path

from .views import PostDetailView

app_name = "posts"

urlpatterns = [
    path("posts/<slug>", PostDetailView.as_view(), name="post_detail"),
]
