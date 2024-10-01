from django.db import models

# Create your models here.
class Especialidades(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    codigo_interno = models.CharField(max_length=5)

    def __str__(self):
        return self.codigo_interno