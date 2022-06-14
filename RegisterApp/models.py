from django.db import models

# Criação do model do uusuário
class User(models.Model):
    UserId = models.AutoField(primary_key=True)
    UserName = models.CharField(max_length=100)
    Email = models.EmailField(max_length=300)
    ContactNumber = models.CharField(max_length=15)
    Adress = models.CharField(max_length=200)
    Profession = models.CharField(max_length=50)
    ResumeFile = models.FileField()

