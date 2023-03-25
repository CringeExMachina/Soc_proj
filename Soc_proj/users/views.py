from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CreationForm

class LogOut(CreateView):
    form_class=CreationForm
    success_url=reverse_lazy('post:General')
    template_name='users/logged_out.html'

class SignUp(CreateView):
    form_class=CreationForm
    success_url=reverse_lazy('post:General')
    template_name = 'users/signup.html'

