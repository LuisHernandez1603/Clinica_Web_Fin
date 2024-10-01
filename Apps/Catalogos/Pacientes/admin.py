from django.contrib import admin

from Apps.Catalogos.Pacientes.models import Pacientes


@admin.register(Pacientes)
# Register your models here.
class PacientesAdmin(admin.ModelAdmin):
    list_display = ['numero_cedula', 'nombres', 'apellidos', 'fecha_nacimiento', 'telefono', 'correo_electronico', 'direccion']
    search_fields = ['numero_cedula', 'nombres']