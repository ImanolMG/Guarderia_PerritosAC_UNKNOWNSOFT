from django.db import models

# Create your models here.


class Clientes(models.Model):
    nombre=models.CharField(max_length=30)
    raza_mascota=models.CharField(max_length=30)
    tipomascota=models.CharField(max_length=8)
    telefono=models.CharField(max_length=20)
    tipo_habitacion=models.CharField(max_length=15)


