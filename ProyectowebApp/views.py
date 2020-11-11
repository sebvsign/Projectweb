from django.shortcuts import render, HttpResponse
from equipos.models import Equipo
from .models import Teams
from .forms import TeamsForm, EquipoForm
from django.contrib.auth.decorators import login_required

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
    equipos = Equipo.objects.all()
    data = {
        'equipos':equipos
    }
    return render(request,"ProyectowebApp/listar_equipos.html", data)



@login_required
def nuevo_team(request):
    data = {
        'form':EquipoForm()
    }

    if request.method == 'POST':
        formulario = EquipoForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Guardado correctamente"

    return render(request,"ProyectowebApp/nuevo_team.html", data )

def equipos_modificar(request, id):
    equipos = Equipo.objects.get(id=id)
    data = {
        'form':EquipoForm(instance=equipos)


    }
    if request.method =='POST':
        formulario = EquipoForm(data=request.POST, instance=equipos)
        if formulario.is_valid():
         formulario.save()
        data['mensaje'] = "Modificado correctamente"
        data['form'] = formulario


    return render(request,'ProyectowebApp/equipos_modificar.html',data)