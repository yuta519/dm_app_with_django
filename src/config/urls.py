from django.contrib import admin
from django.urls import include, path

from app.urls import urlpatterns as app_urls
from app.views.auth import LoginView, logout_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", logout_view, name="logout"),
    path("", include(app_urls)),
]
