from django.contrib import admin
from django.urls import include, path

from app.urls import urlpatterns as app_urls
from app.views.auth import LoginView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", LoginView.as_view()),
    path("", include(app_urls)),
]
