from django.contrib import admin

from Apps.Catalogos.Recepcionistas.models import Recepcionistas


@admin.register(Recepcionistas)
# Register your models here.
class RecepcionistasAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'telefono', 'correo_electronico', 'fecha_ingreso']
    search_fields = ['nombre']