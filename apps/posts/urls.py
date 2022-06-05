from django.urls import path
from .views import PostDetailView

urlpatterns = [
    path("posts/<slug>", PostDetailView.as_view()),
]
