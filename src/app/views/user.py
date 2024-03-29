from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from django.views import generic


class UserListView(LoginRequiredMixin, generic.ListView):
    model = User
    template_name = "users/list.html"

    def get_queryset(self) -> QuerySet[Any]:
        return User.objects.exclude(id=self.request.user.id)


class UserDetailView(LoginRequiredMixin, generic.DetailView):
    model = User
    template_name = "users/detail.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["auth_user"] = self.request.user
        return context
