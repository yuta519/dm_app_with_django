from django import forms


class LoginFormWithUsername(forms.Form):
    # username = forms.CharField()
    email = forms.CharField()
    # email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    ...
