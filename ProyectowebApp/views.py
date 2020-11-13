from django.shortcuts import redirect, render, HttpResponse
from django.shortcuts import render, HttpResponse, redirect
from equipos.models import Equipo
from .models import Teams
from .forms import TeamsForm, EquipoForm, CustomeUserForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, authenticate

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

@login_required
def listado_equipos(request):
    equipos = Equipo.objects.all()
    data = {
        'equipos':equipos
    }
    return render(request,"ProyectowebApp/listar_equipos.html", data)



@permission_required('equipos.add_equipo')
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

@login_required
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

@login_required
def equipos_eliminar(request, id):
    equipos = Equipo.objects.get(id=id)
    equipos.delete()
    return redirect(to="Listado_equipos")

def registro_usuario(request):
    data = {
        'form':CustomeUserForm()
    }

    if request.method =='POST':
        formulario = CustomeUserForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(to='/')
        data["form"] = formulario


    return render(request,'registration/registro.html',data)