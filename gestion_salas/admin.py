from django.contrib import admin
from .models import Sala, Reserva

@admin.register(Sala)
class SalaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'capacidad_maxima', 'habilitada')
    search_fields = ('nombre',)

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('sala', 'rut_persona', 'hora_inicio', 'hora_termino', 'activa')
    list_filter = ('sala', 'activa')

    fieldsets = (
        ('Información de la Reserva', {
            'fields': ('sala', 'rut_persona', 'activa')
        }),
        ('Horas de la Reserva', {
            'fields': ('hora_inicio', 'hora_termino')
        }),
    )