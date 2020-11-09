from django.urls import path

from ProyectowebApp import views

urlpatterns = [
    path('index', views.index, name="Index"),
    path('arsenal', views.arsenal, name="Arsenal"),
    path('acerca', views.acerca, name="Acerca"),
    path('formulario', views.formulario, name="Formulario"),

]