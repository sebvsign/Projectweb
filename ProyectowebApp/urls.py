from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy

from ProyectowebApp import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from .views import error_facebook

urlpatterns = [
    path('', views.index, name="Index"),
    path('arsenal', views.arsenal, name="Arsenal"),
    path('acerca', views.acerca, name="Acerca"),
    path('formulario', views.formulario, name="Formulario"),
    path('equipos', views.equipos, name="Equipos"),
    path('nuevo_equipo', views.nuevo_team, name="Nuevo_team"),
    path('listar_equipos', views.listado_equipos, name="Listado_equipos"),
    path('equipos_modificar/<id>/',views.equipos_modificar, name="Equipo_Modificar"),
    path('equipos_eliminar/<id>/',views.equipos_eliminar, name="Equipo_Eliminar"),
    path('registro',views.registro_usuario, name="registro_usuario"),
    path('error-facebook/', error_facebook, name= 'error_facebook')
    ]


urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)