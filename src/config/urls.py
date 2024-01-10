from django.contrib import admin
from django.urls import include, path

from app.urls import urlpatterns as app_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts", include("django.contrib.auth.urls")),
    path("", include(app_urls)),
]
