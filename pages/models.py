from django.db import models

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
    
class Track(models.Model):
    track=models.CharField(max_length=30)

class Courses(models.Model):
    course=models.CharField(max_length=50)
    track=models.ForeignKey(Track,on_delete=models.CASCADE)
    def __str__(self):
        return f"course for track {self.track}"
class Levels(models.Model):
    level=models.CharField(max_length=20)
    track=models.ForeignKey(Track,models.CASCADE)
    content=models.TextField()

class Material(models.Model):
    material=models.FileField(upload_to='materials/')
    track=models.ForeignKey(Track,on_delete=models.CASCADE)
    def __str__(self):
        return f"course for track {self.track}"
    
class Skills(models.Model):
    skill=models.CharField(max_length=20)
    def __str__(self):
        return self.skill

class Task(models.Model):
    task=models.FileField(upload_to='Tasks/')
    deadline=models.TimeField()
    rate=models.DecimalField(max_digits=10,decimal_places=5)
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"



