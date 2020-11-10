from django.contrib import admin
from .models import Usuario, Regiones, Teams
# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['Nickname', 'Correo', 'asunto', 'Comentario']
    search_fields = ['Nickname', 'Correo']
    list_filter =['Nickname']

class TeamsAdmin(admin.ModelAdmin):
    list_display = ['nombre','etiqueta','logo','region']
    search_fields = ['nombre','region']
    list_filter =['region']

admin.site.register(Usuario,UsuarioAdmin)

admin.site.register(Regiones)
admin.site.register(Teams)
