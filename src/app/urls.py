from django.urls import path

from app.views import (
    ConversationApiViewSet,
    ConversationDetailView,
    ConversationListView,
    UserDetailView,
    UserListView,
)

app_name = "app"

urlpatterns = [
    path("", UserListView.as_view(), name="user_list"),
    path("users/", UserListView.as_view(), name="user_list"),
    path("users/<int:pk>/", UserDetailView.as_view(), name="user_detail"),
    path("conversations/", ConversationListView.as_view(), name="conversation_list"),
    path(
        "conversations/<int:pk>/",
        ConversationDetailView.as_view(),
        name="conversation_detail",
    ),
    path(
        "api/conversations",
        ConversationApiViewSet.as_view({"get": "list", "post": "create"}),
        name="conversation_api",
    ),
    path(
        "api/conversations/<int:pk>",
        ConversationApiViewSet.as_view({"get": "retrieve"}),
        name="conversation_api",
    ),
]
