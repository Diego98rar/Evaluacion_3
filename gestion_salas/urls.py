from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_salas, name='lista_salas'),
    path('sala/<int:pk>/', views.detalle_sala, name='detalle_sala'),
]