from django.urls import path
from django.views.generic.base import TemplateView
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django_filters.views import FilterView
from .filters import RoomFilter, GuestFilter, BookingFilter

from .views import Homeview, Opiniones, LikeView ,EditarHabitacionView, EditarPedidoView, Detalle_Factura,EstadoReservaView, EditarProductoView , EditarPerfilView,PasswordsChangeView, ConfigView, Rooms, Reservar, Detalle_Reserva, EditarProveedorView, EditarHuespedView, AgregarStockView, OcuparStockView, Estado_Pedido, EstadoOrdenView, EditarPlatoView, EditarEmpleadoView

from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    #vistas generales y de usuario común
    path('', Homeview.as_view(), name="index"),
    path('ayuda', views.ayuda, name='ayuda'),
    path('nuevo_post', views.nuevo_post, name='nuevo_post'),
    path('crear_post', views.crear_post, name='crear_post'),
    path('editar_post/<int:id>', views.editar_post, name='editar_post'),
    path('eliminar_post/<int:id>', views.eliminar_post, name='eliminar_post'),
    path('opiniones/<int:pk>', Opiniones.as_view(), name='opiniones'),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('publicar_comentario/<int:pk>', views.publicar_comentario, name='publicar_comentario'),
    path('publicar_respuesta/<int:pk>', views.publicar_respuesta, name='publicar_respuesta'),
    path('login', views.login, name="login"),
    path('logout', views.logout, name='logout'),
    path('registro', views.registro, name="registro"),
    path('dashboard', views.dashboard, name='dashboard'),

    path('perfil/', views.perfil, name='perfil'),
    path('perfil/<str:username>/', views.perfil, name='perfil'),
    path('editar_perfil/<int:pk>', EditarPerfilView.as_view(), name='editar_perfil'),
    path('configuracion/<int:pk>', ConfigView.as_view(), name='configuracion'),
    #path('password/', auth_views.PasswordChangeView.as_view(template_name='chage-password.html')),
    path('password/', PasswordsChangeView.as_view(template_name='chage-password.html')),


    path('mis_facturas', views.mis_facturas, name='mis_facturas'),
    path('mis_reservas', views.mis_reservas, name='mis_reservas'),

    path('all_rooms', views.all_rooms, name='all_rooms'),
    path('detalle_habitacion/<int:pk>', Rooms.as_view(), name='detalle_habitacion'),
    path('reservar/<int:pk>', Reservar.as_view(), name='reservar'),
    path('nueva_reservacion', views.nueva_reservacion, name="nueva_reservacion"),

    #vistas empresa


    #templates usuarios del sistema 
    path('usuarios', views.usuarios, name='usuarios'),
    path('editar_usuario/<int:id>', views.editar_usuario, name='editar_usuario'),
    path('editar_permiso/<int:id>', views.editar_permiso, name='editar_permiso'),
    path('eliminar_usuario/<int:id>', views.eliminar_usuario, name='eliminar_usuario'),

    #templates administracion/habitaciones
    path('habitaciones/', views.habitaciones, name='habitaciones'),
    path('crear_habitacion', views.crear_habitacion, name='crear_habitacion'),
    path('editar_habitacion/<int:pk>', EditarHabitacionView.as_view(), name='editar_habitacion'),
    path('eliminar_habitacion/<int:id>', views.eliminar_habitacion, name='eliminar_habitacion'),

    #templates administracion/platos
    path('comedor/', views.comedor, name='comedor'),
    path('nuevo_plato/', views.nuevo_plato, name='nuevo_plato'),
    path('editar_plato/<int:pk>', EditarPlatoView.as_view(), name='editar_plato'),
    path('eliminar_plato/<int:id>', views.eliminar_plato, name='eliminar_plato'),

    #templates administracion/proveedores
    path('proveedores/', views.proveedores, name='proveedores'),
    path('nuevo_proveedor/', views.nuevo_proveedor, name='nuevo_proveedor'),
    path('editar_proveedor/<int:pk>', EditarProveedorView.as_view(), name='editar_proveedor'),
    path('eliminar_proveedor/<int:id>', views.eliminar_proveedor, name='eliminar_proveedor'),

    #templates administracion/húespedes
    path('huespedes/' , views.huespedes, name='huespedes'),
    path('editar_huesped/<int:pk>', EditarHuespedView.as_view(), name='editar_huesped'),
    path('nuevo_huesped', views.nuevo_huesped, name='nuevo_huesped'),
    path('eliminar_huesped/<int:id>', views.eliminar_huesped, name='eliminar_huesped'),

    #templates administracion/solictud de reservas u orden de compras
    path('orden_compras/' , views.orden_compras, name='orden_compras'),
    path('estado_reserva/<int:pk>', EstadoReservaView.as_view(), name='estado_reserva'),
    path('detalle_reserva/<int:pk>', views.Detalle_Reserva.as_view(), name='detalle_reserva'),
    path('eliminar_solicitud/<int:id>', views.eliminar_solicitud , name='eliminar_solicitud'),

    #templates administracion/facturas
    path('facturas', views.facturas, name='facturas'),
    path('nueva_factura', views.nueva_factura, name='nueva_factura'),
    path('eliminar_factura/<int:id>', views.eliminar_factura, name='eliminar_factura'),
    path('editar_factura/<int:id>', views.editar_factura, name='editar_factura'),
    path('detalle_factura/<int:pk>', Detalle_Factura.as_view(), name='detalle_factura'),

    #templates administracion/trabajadores/cargos
    path('empleados', views.empleados, name='empleados'),
    path('nuevo_empleado', views.nuevo_empleado, name='nuevo_empleado'),
    path('editar_empleado/<int:pk>', EditarEmpleadoView.as_view(), name='editar_empleado'),
    #path('editar_empleado/<int:id>', views.editar_empleado, name='editar_empleado'),
    path('eliminar_empleado/<int:id>', views.eliminar_empleado, name='eliminar_empleado'),

    #templates orden de pedidos
    path('orden_pedido', views.orden_pedido, name='orden_pedido'),
    path('nuevo_pedido', views.nuevo_pedido, name='nuevo_pedido'),
    path('editar_pedido/<int:pk>', EditarPedidoView.as_view(), name='editar_pedido'),
    path('eliminar_pedido/<int:id>', views.eliminar_pedido, name='eliminar_pedido'),
    path('estado_pedido/<int:pk>', Estado_Pedido.as_view(), name='estado_pedido'),

    #tempates repecion de productos
    path('recepcion_productos', views.recepcion_productos, name='recepcion_productos'),
    path('nuevo_producto', views.nuevo_producto, name='nuevo_producto'),
    path('editar_producto/<int:pk>', EditarProductoView.as_view(), name='editar_producto'),
    path('eliminar_producto/<int:id>', views.eliminar_producto, name='eliminar_producto'),
    path('agregar_stock/<int:pk>', AgregarStockView.as_view(), name='agregar_stock'),
    path('ocupar_stock/<int:pk>', OcuparStockView.as_view(), name='ocupar_stock'),


    #templates de proveedor
    path('login_proveedores', views.login_proveedores, name='login_proveedores'),
    path('index_proveedor', views.index_proveedor, name='index_proveedor'),
    path('info_orden/<int:pk>', EstadoOrdenView.as_view(), name='info_orden'),

     
    #reset passwords templates
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
 
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
 
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
 
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),

]