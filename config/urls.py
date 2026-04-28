from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

from user.views import default_redirect_view

urlpatterns = [
    path("", default_redirect_view),
    path("admin/", admin.site.urls),
    path("user/", include("user.urls")),
    path("blog/", include("blog.urls")),
    path("interaction/", include("interaction.urls")),
    path("notification/", include("notification.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    from debug_toolbar.toolbar import debug_toolbar_urls

    urlpatterns += debug_toolbar_urls()
