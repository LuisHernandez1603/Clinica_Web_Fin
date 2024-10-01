from django.contrib import admin

from Apps.Movimientos.Consultas.models import Consultas


@admin.register(Consultas)
# Register your models here.
class ConsultasAdmin(admin.ModelAdmin):
    list_display = ['id_citas', 'descripcion', 'diagnostico', 'recomendaciones']
    search_fields = ['id_citas', 'descripcion']