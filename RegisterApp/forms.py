from django import forms
from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['UserName','Email','ContactNumber','Adress','Profession','ResumeFile']

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['ResumeFile']