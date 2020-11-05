from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):

    return render(request, "ProyectowebApp/index.html")

def servicios(request):

    return render(request, "ProyectowebApp/arsenal.html")

def tienda(request):

    return render(request, "ProyectowebApp/acerca.html")

def blog(request):

    return render(request, "ProyectowebApp/formulario.html")

def contacto(request):

    return render(request, "ProyectowebApp/login.html")
