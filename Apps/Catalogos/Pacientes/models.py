from django.db import models

# Create your models here.
class Pacientes(models.Model):
    numero_cedula = models.CharField(max_length=16)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    fecha_nacimiento = models.DateTimeField()
    telefono = models.CharField(max_length=8)
    correo_electronico= models.CharField(max_length=100, null=True)
    direccion = models.CharField(max_length=100, null= True)

    def __str__(self):
        return self.nombres