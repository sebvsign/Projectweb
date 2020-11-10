from django.shortcuts import render, HttpResponse
from equipos.models import Equipo
from .models import Teams
from .forms import TeamsForm

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

def listado_equipos(request):
    teams = Teams.objects.all()
    data = {
        'teams':teams
    }
    return render(request,"ProyectowebApp/listar_equipos.html", data)




def nuevo_team(request):
    data = {
        'form':TeamsForm()
    }

    if request.method == 'POST':
        formulario = TeamsForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Guardado correctamente"

    return render(request,"ProyectowebApp/nuevo_team.html", data )