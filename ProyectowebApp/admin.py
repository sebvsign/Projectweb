from django.contrib import admin
from .models import Usuario
# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['Nickname', 'Correo', 'asunto', 'Comentario']
    search_fields = ['Nickname', 'Correo']
    list_filter =['Nickname']


admin.site.register(Usuario,UsuarioAdmin)
