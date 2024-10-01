from django.contrib import admin

from Apps.Movimientos.Doctores.models import Doctores


@admin.register(Doctores)
# Register your models here.
class DoctoresAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'telefono', 'correo_electronico', 'id_especialidades']
    search_fields = ['nombre', 'id_especialidades']