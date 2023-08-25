from django.db import models


class Contact(models.Model):
    first_name=models.CharField(max_length=20,verbose_name='First Name')
    last_name=models.CharField(max_length=20,verbose_name='Last Name')
    email=models.EmailField(max_length=20,verbose_name='Email')
    phone_number=models.CharField(max_length=11,verbose_name='Mobile Number')
    message=models.CharField(max_length=500)
    def __str__(self):
        return self.email