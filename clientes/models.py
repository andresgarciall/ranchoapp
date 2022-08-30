from django.db import models


class Servicios(models.Model):
    nombre_servicio=models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_servicio


# Create your models here.
class Cliente(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=80)
    cedula=models.CharField(max_length=11)
    celular=models.CharField(max_length=10)
    direccion=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    servicio=models.ForeignKey(Servicios, on_delete=models.CASCADE, blank=True, null=True)
    fecha_registro=models.DateTimeField('check in')
    fecha_salida=models.DateTimeField('check out')
   
    def __str__(self):
        return f'{self.nombre} {self.apellido}'