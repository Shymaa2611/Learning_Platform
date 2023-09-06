from django.db import models
from pages.models import Track,Levels,Task,Skills
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(models.Model):
    username=models.CharField(max_length=20)
    first_name=models.CharField(max_length=20,verbose_name='First Name')
    last_name=models.CharField(max_length=20,verbose_name='Last Name')
    email=models.EmailField()
    password=models.CharField(max_length=50)
    mobile=models.CharField(max_length=11)
    image=models.ImageField(upload_to='users/photos/',blank=True,null=True)
    track=models.ForeignKey(Track,on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return self.email 

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    level=models.ForeignKey(Levels,on_delete=models.CASCADE,blank=True,null=True)
    task=models.ForeignKey(Task,models.CASCADE,blank=True,null=True)
    skill=models.ManyToManyField(Skills)
    def __str__(self):
        return f"{self.user.username} Profile"
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
