from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.views import generic

from app.forms import LoginFormWithUsername


class LoginView(generic.FormView):
    form_class = LoginFormWithUsername
    template_name = "registration/login.html"

    def form_valid(self, form: LoginFormWithUsername):
        user = authenticate(
            self.request,
            email=form.cleaned_data["email"],
            password=form.cleaned_data["password"],
        )
        if user is not None:
            login(self.request, user)
            return redirect("/")
        else:
            return redirect("/login")
