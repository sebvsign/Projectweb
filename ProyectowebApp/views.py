from django.shortcuts import render, HttpResponse
from equipos.models import Equipo

# Create your views here.
#Profe aca hicimos una prueba de merge con errores (adrer)

def index(request):

    return render(request, "ProyectowebApp/index.html")

def arsenal(request):

    return render(request, "ProyectowebApp/arsenal.html")

def acerca(request):

    return render(request, "ProyectowebApp/acerca.html")

def formulario(request):

    return render(request, "ProyectowebApp/formulario.html")

def equipos(request):
    #importamos todos los objetos que esten en equipo
    equipos= Equipo.objects.all()
    return render(request, "ProyectowebApp/equipos.html", {"equipos": equipos})
