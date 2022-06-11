from django.db import models

# Create your models here.

class User(models.Model):
    UserId = models.AutoField(primary_key=True)
    UserName = models.CharField(max_length=100)
    Email = models.EmailField(max_length=300)
    ContactNumber = models.CharField(max_length=15)
    Adress = models.TextField()
    Profession = models.CharField(max_length=50)
    ResumeFileName = models.CharField(max_length=500)

