# Create routes for the views

from django.urls import path
from app.views import UserListView

app_name = "app"

urlpatterns = [
    # path("", views.index, name="index"),
    path("users/", UserListView.as_view(), name="user_list"),
    # path("users/<int:pk>/", views.UserDetail.as_view()),
    # path("messages/", views.MessageList.as_view()),
    # path("messages/<int:pk>/", views.MessageDetail.as_view()),
    # path("conversations/", views.ConversationList.as_view()),
    # path("conversations/<int:pk>/", views.ConversationDetail.as_view()),
]
