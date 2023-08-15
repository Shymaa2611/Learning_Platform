from django.shortcuts import render
from django.views.generic import ListView,CreateView
from .models import Course,Module,Subject
from .forms import courseForm
class list_course(ListView):
    model=Course
    template_name='list.html'

class create_new_course(CreateView):
    model=Course
    form_class=courseForm
    template_name='create_course.html'
    context_object_name='form'
    success_url='/'

