from django.urls import path

from app.views import (
    ConversationApiViewSet,
    ConversationListView,
    UserDetailView,
    UserListView,
)

app_name = "app"

urlpatterns = [
    path("users/", UserListView.as_view(), name="user_list"),
    path("users/<int:pk>/", UserDetailView.as_view(), name="user_detail"),
    path("conversations/", ConversationListView.as_view(), name="conversation_list"),
    path(
        "api/conversations",
        ConversationApiViewSet.as_view({"get": "list", "post": "create"}),
        name="conversation_api",
    ),
]
