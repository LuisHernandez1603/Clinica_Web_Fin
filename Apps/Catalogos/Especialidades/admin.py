from django.contrib import admin

from Apps.Catalogos.Especialidades.models import Especialidades


@admin.register(Especialidades)
# Register your models here.
class EspecialidadesAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion', 'codigo_interno']
    search_fields = ['codigo_interno', 'nombre']