from django.urls import path

from ProyectowebApp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('index', views.index, name="Index"),
    path('arsenal', views.arsenal, name="Arsenal"),
    path('acerca', views.acerca, name="Acerca"),
    path('formulario', views.formulario, name="Formulario"),
    path('equipos', views.equipos, name="Equipos"),
]


urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)