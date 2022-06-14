from django import forms
from .models import User

# Formulário de criação
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['UserName','Email','ContactNumber','Adress','Profession','ResumeFile']

# Formulário de edição
class UpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['UserName','Email','ContactNumber','Adress','Profession']
