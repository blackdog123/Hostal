from django.urls import path
from . import views
from django.conf.urls import url
from django_filters.views import FilterView
from .filters import RoomFilter, GuestFilter, BookingFilter

from .views import DashboardView, Homeview, Opiniones, ReservaView, Detalle_Factura

from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    #vistas generales y de usuario común
    path('', Homeview.as_view(), name="index"),
    path('opiniones/<int:pk>', Opiniones.as_view(), name='opiniones'),
    path('publicar_comentario/<int:pk>', views.publicar_comentario, name='publicar_comentario'),
    path('login', views.login, name="login"),
    path('logout', views.logout, name='logout'),
    path('registro', views.registro, name="registro"),
    path('dashboard', DashboardView.as_view(), name='dashboard'),
    path('perfil/', views.perfil, name='perfil'),
    path('perfil/<str:username>/', views.perfil, name='perfil'),
    path('editar_perfil/<int:user_id>', views.editar_perfil, name='editar_perfil'),
    #path('agregar_trabajador', views.agregar_trabajador, name='agregar_trabajador'),
    path('guardar_trabajador', views.guardar_trabajador, name='guardar_trabajador'),
    path('editar_trabajador/<int:id>', views.editar_trabajador, name='editar_trabajador'),
    path('eliminar_trabajador/<int:id>', views.eliminar_trabajador, name='eliminar_trabajador'),
    path('reservar/' , ReservaView.as_view(), name='reservar'),
    path('mis_facturas', views.mis_facturas, name='mis_facturas'),
    path('mis_reservas', views.mis_reservas, name='mis_reservas'),
    path('configuracion/<int:id>', views.configuracion, name='configuracion'),

    #vistas empleado
    path('login_empleados', views.login_empleados, name="login_empleados"),

    #vistas empresa

    #templates administracion/habitaciones
    path('habitaciones/', views.habitaciones, name='habitaciones'),
    path('crear_habitacion', views.crear_habitacion, name='crear_habitacion'),
    path('editar_habitacion/<int:id>', views.editar_habitacion, name='editar_habitacion'),
    path('eliminar_habitacion/<int:id>', views.eliminar_habitacion, name='eliminar_habitacion'),

    #templates administracion/platos
    path('comedor/', views.comedor, name='comedor'),
    path('nuevo_plato/', views.nuevo_plato, name='nuevo_plato'),
    path('editar_plato/<int:id>', views.editar_plato, name='editar_plato'),
    path('eliminar_plato<int:id>', views.eliminar_plato, name='eliminar_plato'),

    #templates administracion/proveedores
    path('proveedores/', views.proveedores, name='proveedores'),
    path('nuevo_proveedor/', views.nuevo_proveedor, name='nuevo_proveedor'),
    path('editar_proveedor/<int:id>', views.editar_proveedor, name='editar_proveedor'),
    path('eliminar_proveedor<int:id>', views.eliminar_proveedor, name='eliminar_proveedor'),

    #templates administracion/húespedes
    path('huespedes/' , views.huespedes, name='huespedes'),
    path('editar_huesped/<int:id>', views.editar_huesped, name='editar_huesped'),
    path('nuevo_huesped', views.nuevo_huesped, name='nuevo_huesped'),
    path('eliminar_huesped/<int:id>', views.eliminar_huesped, name='eliminar_huesped'),

    #templates administracion/solictud de reservas
    path('solicitud_reservas/' , views.solicitud_reservas, name='solicitud_reservas'),
    path('ver_estado/<int:id>', views.ver_estado, name='ver_estado'),
    path('eliminar_solicitud/<int:id>', views.eliminar_solicitud , name='eliminar_solicitud'),

    #templates administracion/facturas
    path('facturas', views.facturas, name='facturas'),
    path('nueva_factura', views.nueva_factura, name='nueva_factura'),
    path('eliminar_factura/<int:id>', views.eliminar_factura, name='eliminar_factura'),
    path('detalle_factura/<int:pk>', Detalle_Factura.as_view(), name='detalle_factura')
]