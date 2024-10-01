from django.db import models
from Apps.Catalogos.Pacientes.models import Pacientes
from Apps.Catalogos.Recepcionistas.models import Recepcionistas
from Apps.Movimientos.Doctores.models import Doctores

# Create your models here.
class Citas(models.Model):
    confirmacion = models.BooleanField()
    fecha_hora = models.DateTimeField()
    id_pacientes = models.ForeignKey(Pacientes, on_delete= models.RESTRICT
    )
    id_doctores = models.ForeignKey(Doctores, on_delete=models.RESTRICT)
    id_recepcionistas = models.ForeignKey(Recepcionistas, on_delete=models.RESTRICT)