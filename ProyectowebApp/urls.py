from django.urls import path

from ProyectowebApp import views
from django.conf import settings
from django.conf.urls.static import static


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
]


urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)