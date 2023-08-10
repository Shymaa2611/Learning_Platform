from django.db import models
from django.contrib.auth.models import User

class Subject(models.Model):
    title=models.CharField(max_length=50)
    def __str__(self):
        return self.title

class Course(models.Model):
    owner = models.ForeignKey(User,related_name='courses_created',on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject,related_name='courses',on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    overview = models.TextField()
