from django import forms
from .models import Reserva

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['rut_persona']
        labels = {
            'rut_persona': 'RUT (sin puntos y con guion, ej: 12345678-9)'
        }
        widgets = {
            'rut_persona': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': '12345678-9'}
            ),
        }