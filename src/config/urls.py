from django.urls import include, path

from app.admin import admin_site
from app.urls import urlpatterns as app_urls
from app.views.auth import LoginView, logout_view

urlpatterns = [
    path("admin/", admin_site.urls),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", logout_view, name="logout"),
    path("", include(app_urls)),
]
