from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.views import generic

from app.forms import LoginForm


class LoginView(generic.FormView):
    form_class = LoginForm
    template_name = "auth/login.html"

    def form_valid(self, form):
        user = authenticate(
            self.request,
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password"],
        )
        if user is not None:
            login(self.request, user)
            return redirect("home")
        else:
            return redirect("login")
