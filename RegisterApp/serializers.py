from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from RegisterApp.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('UserId','UserName','Email','ContactNumber','Adress','Profession','ResumeFileName')