from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.shortcuts import render, redirect

from . import forms


class LoginUser(LoginView):
    form_class = forms.UserLoginForm
    template_name = 'users/login.html'


def logout_user(request):
    logout(request)
    return redirect('login_user')
