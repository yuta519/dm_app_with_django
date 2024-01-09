from django.contrib.auth.models import User
from django.views import generic


class UserListView(generic.ListView):
    model = User
    template_name = "users/list.html"


class UserDetailView(generic.DetailView):
    model = User
    template_name = "users/detail.html"
