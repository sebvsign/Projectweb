from django.shortcuts import render, HttpResponse

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

    return render(request, "ProyectowebApp/equipos.html")
