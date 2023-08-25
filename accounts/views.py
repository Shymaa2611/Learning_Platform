from django.shortcuts import render
from django.views.generic import CreateView
from .forms import authenticationForm
from django.contrib.auth.models import User

class signUp(CreateView):
    form_class=authenticationForm
    context_object_name='form'
    template_name='authentication/signUp.html'
    success_url='/'
