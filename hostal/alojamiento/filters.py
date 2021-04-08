from django.contrib.auth.models import User
import django_filters
from django import forms 

from .models import *

class RoomFilter(django_filters.FilterSet):
    precio = django_filters.CharFilter(lookup_expr='icontains', label="Precio")
    
    class Meta:
        model = Room
        fields = ['tipo_habitacion','numero_habitacion','tipo_cama', 'precio', 'estado', ]


class GuestFilter(django_filters.FilterSet):

    nombre = django_filters.CharFilter(lookup_expr='icontains', label="Nombre")
    apellido = django_filters.CharFilter(lookup_expr='icontains', label="Apellido")

    class Meta:
        model = Guest
        fields = ['nombre','apellido','empresa','habitacion','estado_huesped']


class BookingFilter(django_filters.FilterSet):

    class Meta:
        model = Booking_Client
        fields = ['estado','user',]


class TicketFilter(django_filters.FilterSet):

    class Meta:
        model = Ticket
        fields = [ 'to_user',]

        
class ProviderFilter(django_filters.FilterSet):
    id = django_filters.CharFilter(lookup_expr='icontains', label="Id")
    rubro = django_filters.CharFilter(lookup_expr='icontains', label="Rubro")

    class Meta:
        model = Proovider
        fields = ['id','rubro',]


class DishesFilter(django_filters.FilterSet):

    class Meta:
        model = Dishes
        fields = ['dia','categoria',]