from django.urls import path
from . import views

urlpatterns = [
    path('signup/',view=views.authentications,name='signUp'),
    #path('login/',view=views.login,name='login'),
    path('profile/',view=views.profile,name='profile'),
    path('settings/',view=views.settings,name='settings'),
   
    
]
