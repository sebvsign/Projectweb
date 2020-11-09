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