from django.contrib import admin
from django.urls import include, path

from app.urls import urlpatterns as app_urls
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", auth_views.LoginView.as_view()),
    path("", include(app_urls)),
]
