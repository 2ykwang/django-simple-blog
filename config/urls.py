from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.posts.urls")),
]

if settings.ENABLE_SILK:
    urlpatterns += [
        path("silk/", include("silk.urls", namespace="silk")),
    ]

if settings.ENABLE_DEBUG_TOOLBAR:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
