from django.db import models
from django.utils import timezone
from datetime import timedelta

class Sala(models.Model):
    nombre = models.CharField(max_length=100)
    capacidad_maxima = models.IntegerField()
    habilitada = models.BooleanField(default=True) 

    def __str__(self):
        return self.nombre

    def esta_disponible(self):
        """Verifica si la sala tiene una reserva activa AHORA."""
        ahora = timezone.now()
        reservas_activas = self.reserva_set.filter(
            hora_inicio__lte=ahora, # Que empezó en el pasado
            hora_termino__gte=ahora,  # Y que aún no termina
            activa=True
        )
        return not reservas_activas.exists()

class Reserva(models.Model):
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    rut_persona = models.CharField(max_length=12)
    hora_inicio = models.DateTimeField()
    hora_termino = models.DateTimeField()
    activa = models.BooleanField(default=True)

    def __str__(self):
        return f"Reserva de {self.sala.nombre} por {self.rut_persona}"

    def save(self, *args, **kwargs):
        
        if not self.id:
            if not getattr(self, 'hora_inicio', None):
                self.hora_inicio = timezone.now()
            if not getattr(self, 'hora_termino', None):
                self.hora_termino = self.hora_inicio + timedelta(hours=2)
            self.activa = True
        super().save(*args, **kwargs)

    def esta_activa(self):
        ahora = timezone.now()
        return self.activa and (self.hora_inicio <= ahora <= self.hora_termino)