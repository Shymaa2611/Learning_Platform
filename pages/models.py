from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    first_name=models.CharField(max_length=20,verbose_name='First Name')
    last_name=models.CharField(max_length=20,verbose_name='Last Name')
    email=models.EmailField(max_length=20,verbose_name='Email')
    phone_number=models.CharField(max_length=11,verbose_name='Mobile Number')
    message=models.CharField(max_length=500)
    def __str__(self):
        return self.email
    

class Blog(models.Model):
    title=models.CharField(max_length=20,verbose_name='Title')
    image=models.ImageField(upload_to='blog/')
    description=models.CharField(max_length=200)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    

