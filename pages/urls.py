from django.urls import path

from . import views

urlpatterns = [
   path('', views.list_course.as_view(), name='list'),
   path('create_form/', views.create_new_course.as_view(), name='create_form'),

]

