from django import forms
from django.forms import ModelForm
from .models import Teams

class TeamsForm(ModelForm):

    class Meta:
        model = Teams
        fields = ['nombre', 'etiqueta', 'logo', 'region']
        