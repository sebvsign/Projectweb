from django import forms
from django.forms import ModelForm
from equipos.models import Equipo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class EquipoForm(ModelForm):
    class Meta:
        model = Equipo
        fields = ['titulo', 'contenido', 'imagen']
        
#no llama los campos completos de django, ver.
class CustomeUserForm(UserCreationForm):
    
    class meta:
        model = User
        fields = ["username","password1","password2", "first_name","last_name","email"]
        

