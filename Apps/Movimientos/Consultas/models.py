from django.db import models

from Apps.Movimientos.Citas.models import Citas


# Create your models here.
class Consultas(models.Model):
    id_citas = models.ForeignKey(Citas, on_delete=models.RESTRICT)
    descripcion = models.CharField(max_length=100)
    diagnostico = models.TextField()
    recomendaciones = models.TextField()

    def __str__(self):
        return self.diagnostico