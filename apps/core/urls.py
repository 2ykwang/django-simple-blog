from django.urls import path
from markdownx.views import MarkdownifyView

from .views import CustomImageUploadView

app_name = "core"

urlpatterns = [
    path("editor/upload/", CustomImageUploadView.as_view(), name="markdownx_upload"),
    path(
        "editor/markdownify/", MarkdownifyView.as_view(), name="markdownx_markdownify"
    ),
]
