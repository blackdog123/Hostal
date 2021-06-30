from django.contrib.auth.models import User
import django_filters
from django import forms 

from .models import *

class UserFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(lookup_expr='icontains', label="Nombre de Usuario" )

    model = User
    fields = ['username',]

class RoomFilter(django_filters.FilterSet):
    numero_habitacion = django_filters.CharFilter(lookup_expr='icontains', label="N° Habitación" )
    precio = django_filters.NumberFilter(lookup_expr='icontains', label="Precio" )
    
    class Meta:
        model = Room
        fields = ['tipo_habitacion','numero_habitacion','tipo_cama', 'precio', 'estado', ]

class RoomUserFilter(django_filters.FilterSet):

    precio = django_filters.NumberFilter(lookup_expr='icontains', label="Precio")

    class Meta:
        model = Room
        fields = ['tipo_habitacion','tipo_cama', 'precio',]



class GuestFilter(django_filters.FilterSet):

    nombre = django_filters.CharFilter(lookup_expr='icontains', label="Nombre")
    apellido = django_filters.CharFilter(lookup_expr='icontains', label="Apellido")
    rut = django_filters.CharFilter(lookup_expr='icontains', label="Rut")

    class Meta:
        model = Guest
        fields = ['nombre','apellido','rut','empresa','habitacion','estado_huesped']


class BookingFilter(django_filters.FilterSet):

    class Meta:
        model = Booking_Client
        fields = ['estado','user',]


class TicketFilter(django_filters.FilterSet):

    class Meta:
        model = Ticket
        fields = ['receptor', 'estado_ticket',]

        
class ProviderFilter(django_filters.FilterSet):
    rubro = django_filters.CharFilter(lookup_expr='icontains', label="Rubro")

    class Meta:
        model = Proovider
        fields = ['empresa', 'rubro',]


class DishesFilter(django_filters.FilterSet):

    class Meta:
        model = Dishes
        fields = ['dia','categoria',]


class EmployeeFilter(django_filters.FilterSet):
    nombre      = django_filters.CharFilter(lookup_expr='icontains', label="Nombre")
    apellido    = django_filters.CharFilter(lookup_expr='icontains', label="Apellido")
    rut         = django_filters.CharFilter(lookup_expr='icontains', label="Rut")

    class Meta:
        model = Employee
        fields = ['nombre', 'apellido', 'rut', 'cargo',]


class OrderProoviderFilter(django_filters.FilterSet):
    producto         = django_filters.CharFilter(lookup_expr='icontains', label="Producto")

    class Meta:
        model = Order
        fields = ['proveedor', 'producto', 'estado',]


class ProductFilter(django_filters.FilterSet):
    stock         = django_filters.CharFilter(lookup_expr='icontains', label="Stock")

    class Meta: 
        model = Product
        fields = ['codigo_producto', 'stock', 'categoria', 'producto', 'tipo_producto',]