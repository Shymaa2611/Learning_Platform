from django.db import models
from pages.models import Track,Levels,Task,Skills
from django.db.models.signals import post_save
class User(models.Model):
    username=models.CharField(max_length=20)
    first_name=models.CharField(max_length=20,verbose_name='First Name')
    last_name=models.CharField(max_length=20,verbose_name='Last Name')
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=50)
    mobile=models.CharField(max_length=11)
    image=models.ImageField(upload_to='users/photos/')
    track=models.ForeignKey(Track,on_delete=models.CASCADE)
    def __str__(self):
        return self.email 

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    level=models.ForeignKey(Levels,on_delete=models.CASCADE)
    task=models.ForeignKey(Task,models.CASCADE)
    skill=models.ManyToManyField(Skills)
    def __str__(self):
        return f"{self.user.username} Profile"
    
def create_profile(sender,**kwargs):
    if kwargs['created']:
        user_profile=Profile.objects.create(user=kwargs['instance'])
post_save.connect(create_profile,sender=User)
        