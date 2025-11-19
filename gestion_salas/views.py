from django.shortcuts import render, get_object_or_404, redirect
from .models import Sala, Reserva
from .forms import ReservaForm
from django.utils import timezone

def lista_salas(request):
    ahora = timezone.now()
    reservas_vencidas = Reserva.objects.filter(
        activa=True, 
        hora_termino__lt=ahora
    )
    
    if reservas_vencidas.exists():
        reservas_vencidas.update(activa=False)


    salas = Sala.objects.filter(habilitada=True) 
    context = {
        'salas': salas
    }
    return render(request, 'lista_salas.html', context)

def detalle_sala(request, pk):
    sala = get_object_or_404(Sala, pk=pk)
    ahora = timezone.now()
    
    if sala.esta_disponible():
        form = ReservaForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                reserva = form.save(commit=False)
                reserva.sala = sala
                reserva.save() 
                return redirect('lista_salas') 
        
        context = {
            'sala': sala,
            'form': form
        }

        return render(request, 'detalle_sala_disponible.html', context)
    
    else:
        reserva_activa = sala.reserva_set.get(
            hora_inicio__lte=ahora,
            hora_termino__gte=ahora,
            activa=True
        )
        context = {
            'sala': sala,
            'reserva': reserva_activa
        }

        return render(request, 'detalle_sala_reservada.html', context)