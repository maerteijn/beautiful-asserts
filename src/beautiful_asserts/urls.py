from django.conf import settings
from django.contrib import admin
from django.urls import path

from .views import ArticleCreateView, ArticleListView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", ArticleListView.as_view(), name="article-list"),
    path("article-create/", ArticleCreateView.as_view(), name="article-create"),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
