from django.db import models

from Apps.Catalogos.Especialidades.models import Especialidades


# Create your models here.
class Doctores(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=8)
    correo_electronico = models.CharField(max_length=100)
    id_especialidades =models.ForeignKey(Especialidades, on_delete=models.RESTRICT)

    def __str__(self):
        return self.nombre