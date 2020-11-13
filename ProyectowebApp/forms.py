from django import forms
from django.forms import ModelForm
from equipos.models import Equipo
from .models import Teams
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TeamsForm(ModelForm):

    class Meta:
        model = Teams
        fields = ['nombre', 'etiqueta', 'logo', 'region']


class EquipoForm(ModelForm):
    class Meta:
        model = Equipo
        fields = ['titulo', 'contenido', 'imagen']
        

class CustomeUserForm(UserCreationForm):
    
    class meta:
        model = User
        fields = ["first_name","last_name","email","username","password1","password2"]

