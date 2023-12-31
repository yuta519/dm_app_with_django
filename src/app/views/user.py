from django.views import generic

from app.models import User


class UserListView(generic.ListView):
    model = User
    template_name = "users/list.html"
