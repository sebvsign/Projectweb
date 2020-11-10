from django.db import models

# Create your models here.
class Usuario(models.Model):
    Nickname = models.CharField(max_length=200)
    Correo = models.CharField(max_length=200)
    asunto = models.CharField(max_length=200)
    Comentario = models.CharField(max_length=1000)

    def __str__(self):
        return self.Nickname

# reinicio de la prueba unitaria

class Regiones(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class Teams(models.Model):
    nombre = models.CharField(max_length=200)
    etiqueta = models.CharField(max_length=5)
    logo =  models.ImageField(upload_to='equipos')
    region = models.ForeignKey(Regiones, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
       