from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path

from apps.posts.sitemaps import (
    CategorySitemap,
    PageSitemap,
    PostSitemap,
    PostsStaticSitemap,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.posts.urls")),
    path("", include("apps.main.urls")),
    path("", include("apps.core.urls")),
    path(
        "sitemap.xml",
        sitemap,
        {
            "sitemaps": {
                "posts": PostSitemap,
                "pages": PageSitemap,
                "categories": CategorySitemap,
                "posts_static": PostsStaticSitemap,
            }
        },
        name="django.contrib.sitemaps.views.sitemap",
    ),
]
handler404 = "apps.core.views.handler404"

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.ENABLE_SILK:
    urlpatterns += [
        path("silk/", include("silk.urls", namespace="silk")),
    ]

if settings.ENABLE_DEBUG_TOOLBAR:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
