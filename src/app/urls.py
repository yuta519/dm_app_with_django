from django.urls import path
from app.views import ConversationListView, UserDetailView, UserListView

app_name = "app"

urlpatterns = [
    path("users/", UserListView.as_view(), name="user_list"),
    path("users/<int:pk>/", UserDetailView.as_view(), name="user_detail"),
    path("conversations/", ConversationListView.as_view(), name="conversation_list"),
    # path("conversations/<int:pk>/", views.ConversationDetail.as_view()),
]
