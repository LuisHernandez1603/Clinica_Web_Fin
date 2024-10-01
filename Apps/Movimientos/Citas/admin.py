from django.contrib import admin

from Apps.Movimientos.Citas.models import Citas


@admin.register(Citas)
# Register your models here.
class CitasAdmin(admin.ModelAdmin):
    list_display = ['confirmacion', 'fecha_hora', 'id_pacientes', 'id_doctores', 'id_recepcionistas']
    search_fields = ['confirmacion']