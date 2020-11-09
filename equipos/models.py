from django.db import models
from django.db.models.deletion import SET_DEFAULT
from django.db.models.fields.related import create_many_to_many_intermediary_model

# Create your models here.

class Equipo(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='equipos')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'equipo'
        verbose_name_plural = 'equipos'

    def __str__(self):
        return self.titulo