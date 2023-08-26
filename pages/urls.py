from django.urls import path

from . import views

urlpatterns = [
  path('',view=views.home,name='index'),
  path('about/',view=views.about,name='about'),
  path('contact/',view=views.contact,name='contact'),
  path('blog/',view=views.blog,name='blog'),
  path('chat/',view=views.chat,name='chat')
] 

