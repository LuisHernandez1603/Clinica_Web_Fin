from django.db import models

# Create your models here.
class Recepcionistas(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=8)
    correo_electronico = models.CharField(max_length=100, null=True)
    fecha_ingreso = models.DateTimeField()

    def __str__(self):
        return self.nombre