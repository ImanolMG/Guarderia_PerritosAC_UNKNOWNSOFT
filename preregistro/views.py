from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.conf import settings
from django.contrib import messages
from .models import Clientes
# Create your views here.


def pagina_principal (request):
    return render(request, "home.html")

def formulario_preregistro (request):
    return render(request, "formulario_preregistro.html")


def registrar_cliente (request):
    nombre = request.POST['txtnombre']
    raza_mascota = request.POST['txtraza']
    tipomascota = request.POST['txttipomascota']
    telefono = request.POST['txttelefono']
    tipo_habitacion = request.POST['tipohabitacion']

    cliente = Clientes.objects.create(
        nombre=nombre, raza_mascota=raza_mascota, tipomascota= tipomascota, telefono = telefono, tipo_habitacion = tipo_habitacion
    )
    messages.success(request, 'Tus datos han sido registrados exitosamente, pronto de contactaremos :)')
    return redirect('/preregistro/')


def administracion_clientes (request):
    lista_preregistros = Clientes.objects.all()
    return render(request, "administracion.html" , {"clientes":lista_preregistros})

def eliminar_cliente (request, id):
    cliente = Clientes.objects.get(id=id)
    cliente.delete()
    return redirect('/administracion/')
