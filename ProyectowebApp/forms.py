from django import forms
from django.forms import ModelForm
from equipos.models import Equipo
from .models import Teams

class TeamsForm(ModelForm):

    class Meta:
        model = Teams
        fields = ['nombre', 'etiqueta', 'logo', 'region']


class EquipoForm(ModelForm):
    class Meta:
        model = Equipo
        fields = ['titulo', 'contenido', 'imagen']
        