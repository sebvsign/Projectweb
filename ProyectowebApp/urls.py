from django.urls import path

from ProyectowebApp import views

urlpatterns = [
    path('index', views.home, name="Index"),
    path('arsenal', views.servicios, name="Arsenal"),
    path('acerca', views.tienda, name="Acerca"),
    path('formulario', views.blog, name="Formulario"),
]