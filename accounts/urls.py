from django.urls import path
from . import views

urlpatterns = [
    path('signup/',view=views.signup,name='signUp'),
    path('profile/',view=views.profile,name='profile'),
    path('settings/',view=views.settings,name='settings'),
    
]
