from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.

#info de la hostal en el index
class Post(models.Model):
    user                = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    fecha_creacion      = models.DateTimeField(default=timezone.now)
    Titulo              = models.CharField(max_length=100, null=True, blank=True)
    imagen              = models.ImageField(upload_to='imagenes', null=True, blank=True)
    likes               = models.ManyToManyField(User, related_name="blog_posts")

    class Meta:
        ordering = ['fecha_creacion']

    def _str_(self):
        return f'{self.user.username}: {self.content}'
    
    def total_likes(self):
        return self.likes.count()



class Comment(models.Model):
    post                = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user                = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion      = models.DateTimeField(default=timezone.now)
    texto               = models.TextField()

    class Meta:
        ordering = ['fecha_creacion']

    def __str__(self):
        return f'{self.user.username}: comentario post_id {self.post.id}'
    
class Answer(models.Model):
    comment             = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='answers')
    user                = models.ForeignKey(User, on_delete=models.CASCADE)   
    fecha_creacion      = models.DateTimeField(default=timezone.now)
    texto               = models.TextField()

    class Meta:
        ordering = ['fecha_creacion']

    def __str__(self):
        return f'{self.user.username}: comentario respuesta id {self.comment.id}'


#----------------------------------------------------------------------#

permissions_choice = (
    ('Administrador', 'Administrador'),
    ('Ayudante Cocina', 'Ayudante Cocina'),
    ('Proveedor', 'Proveedor'),
    ('Recepcionista', 'Recepcionista'),
    ('Solicitante', 'Solicitante'),
    ('Usuario', 'Usuario'),
)


class Profile(models.Model):
    user                    = models.OneToOneField(User, on_delete=models.CASCADE)
    bio                     = models.TextField(max_length=255 ,blank=True, null=True)  
    telefono                = models.CharField(max_length=9, null=True, blank=True)
    foto_perfil             = models.ImageField(default='user_default.png', upload_to='fotos_perfil')
    foto_portada            = models.ImageField(default='portada_default.png', upload_to='fotos_portadas')
    twitter                 = models.CharField(max_length=50, null=True, blank=True)
    instagram               = models.CharField(max_length=50, null=True, blank=True)
    facebook                = models.CharField(max_length=50, null=True, blank=True)
    tipo_permiso            = models.CharField(max_length=50, null=True, blank=False, default='Usuario', choices=permissions_choice)

    def __str__(self):
        return f' perfil de {self.user.username}'


permissions_choice = (
    ('Sin Cargo', 'Sin Cargo'),
    ('Administrador', 'Administrador'),
    ('Ayudante Cocina', 'Ayudante Cocina'),
    ('Recepcionista', 'Recepcionista'),
    ('Solicitante', 'Solicitante'),
)


class Employee(models.Model):
    nombre                  = models.CharField(max_length=255, null=True, blank=False)
    apellido                = models.CharField(max_length=255, null=True, blank=False)
    rut                     = models.CharField(max_length=9, null=True, blank=False)
    cargo                   = models.CharField(max_length=50, null=True, blank=False, default='Sin Cargo', choices=permissions_choice)
    

 
    def __str__(self):
        return f' id {self.id} - {self.nombre} {self.apellido} - {self.cargo} '


# ignorar estos 4 modelos ***************************************

class PriceNight(models.Model):
    cantidad_noches       = models.CharField(max_length=255, null=True, blank=True)
    precio                 = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.cantidad_noches}'

class PriceRoom(models.Model):
    tipo_habitacion         = models.CharField(max_length=255, null=True, blank=True)
    precio                 = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.tipo_habitacion}'

class PricePeople(models.Model):
    cantidad_peronas       = models.CharField(max_length=255, null=True, blank=True)
    precio                 = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.cantidad_peronas}'

class Number(models.Model):
    numero_habitacion       = models.TextField()

    def __str__(self):
        return f'{self.numero_habitacion}'

#*********************************************************************************    

class Type(models.Model):
    tipo_cama               = models.TextField()

    def __str__(self):
        return f'{self.tipo_cama}'


type_room_choice = (
    ('Individual', 'Individual'),
    ('Compartida', 'Compartida'),
 
)

estate_choice = (
    ('Disponible', 'Disponible'),
    ('Ocupada', 'Ocupada'),
    ('En Mantenimiento', 'En Mantenimiento'), 
)

class Room(models.Model):  
    tipo_habitacion         = models.CharField(max_length=50, null=True, blank=False, choices=type_room_choice)
    numero_habitacion       = models.CharField(max_length=100, null=True, blank=False)
    estado                  = models.CharField(max_length=50, null=True, blank=False, choices=estate_choice)
    tipo_cama               = models.ForeignKey(Type, on_delete=models.CASCADE, related_name="types")
    cantidad_camas          = models.CharField(max_length=2, null=True, blank=False)
    cantidad_personas       = models.CharField(max_length=2, null=True, blank=False)
    accesorios              = models.TextField(max_length=255, null=True, blank=True)
    imagen_habitacion       = models.ImageField(default='no_image.png' ,upload_to='habitaciones', null=True, blank=True)
    precio                  = models.CharField(max_length=255, null=True, blank=False) 


    def __str__(self):
        return f'N° Habitación : {self.numero_habitacion} - {self.estado} - {self.tipo_habitacion} - {self.precio}'



huesped_choice = (
    ('En Alojamiento', 'En Alojamiento'),
    ('Retirado', 'Retirado'),
)



class Guest(models.Model):      
    tiempo_transcurrido     = models.DateTimeField(default=timezone.now) 
    empresa                 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enterprises')
    habitacion              = models.ForeignKey(Room, on_delete=models.CASCADE,  related_name='rooms')
    fecha_ingreso           = models.DateField(null=True, blank=False)
    fecha_salida            = models.DateField(null=True, blank=False)
    nombre                  = models.CharField(max_length=255, null=True, blank=False) 
    apellido                = models.CharField(max_length=255, null=True, blank=False) 
    rut                     = models.CharField(max_length=9, null=True, blank=False)  
    estado_huesped          = models.CharField(default="En Alojamiento",max_length=50, null=True, blank=False, choices=huesped_choice)

    def __str__(self):
        return f'{self.habitacion} - {self.empresa} - {self.estado_huesped}'


solicitud_choise = (
    ('En Revision', 'En Revision'),
    ('Aceptada', 'Aceptada'),
    ('Rechazada', 'Rechazada'),
)

class Booking_Client(models.Model):
    user                    = models.ForeignKey(User, on_delete=models.CASCADE, related_name='booking_clients')
    fecha_creacion          = models.DateTimeField(default=timezone.now)
    fecha_llegada           = models.DateField(null=True, blank=True)
    fecha_salida            = models.DateField(null=True, blank=True)
    numero_habitacion       = models.CharField(max_length=50, null=True, blank=True)
    tipo_habitacion         = models.CharField(max_length=50, null=True, blank=True)
    tipo_cama               = models.CharField(max_length=50, null=True, blank=True)
    precio                  = models.CharField(max_length=50, null=True, blank=True)    
    cantidad_camas          = models.CharField(max_length=50, null=True, blank=True)
    nombre                  = models.CharField(max_length=50, null=True, blank=True)
    apellido                = models.CharField(max_length=80, null=True, blank=True)
    rut                     = models.CharField(max_length=80, null=True, blank=True)
    nombre2                 = models.CharField(max_length=50, null=True, blank=True)
    apellido2               = models.CharField(max_length=80, null=True, blank=True)
    rut2                    = models.CharField(max_length=80, null=True, blank=True)
    mensaje                 = models.TextField(max_length=255 ,blank=True, null=True)
    estado                  = models.CharField(max_length=50,default="En Revision" ,null=True, blank=False, choices=solicitud_choise)

    def __str__(self):
        return f'Reserva de : {self.user.username}'
    
  

estado_ticket_choice = (
    ('Sin pagar', 'Sin pagar'),
    ('Pagada', 'Pagada'),
    ('Anulada', 'Anulada'),
)


class Ticket(models.Model):
    hora_creacion           = models.DateTimeField(default=timezone.now)
    fecha_boleta            = models.DateField(null=True, blank=False)
    habitacion_reservada    = models.ForeignKey(Room, on_delete=models.CASCADE , related_name='habitaciones')
    precio_servicio        = models.CharField(max_length=50, null=True, blank=False)
    cantidad_dias           = models.CharField(max_length=50, null=True, blank=False)
    precio_dias             = models.CharField(max_length=50, null=True, blank=False)
    subtotal                = models.CharField(max_length=50, null=True, blank=False)
    iva                     = models.CharField(max_length=50, null=True, blank=False)
    total                   = models.CharField(max_length=50, null=True, blank=False)
    estado_ticket           = models.CharField(default="Sin pagar", max_length=50, null=True, blank=False, choices=estado_ticket_choice)
    remitente               = models.ForeignKey(User, default="1", related_name='user1', on_delete=models.CASCADE)
    receptor                = models.ForeignKey(User, related_name='tickets', on_delete=models.CASCADE)

    def __str__(self):
        return f' Factura {self.remitente} a {self.receptor}'



class Proovider(models.Model):
    fecha_creacion          = models.DateTimeField(default=timezone.now)
    empresa                 = models.ForeignKey(User, on_delete=models.CASCADE)
    rubro                   = models.CharField(max_length=80, null=True, blank=False)
   
    def __str__(self):
        return f'{self.empresa}'


days_choise = (
    ('Lunes', 'Lunes'),
    ('Martes', 'Martes'),
    ('Miércoles', 'Miércoles'),
    ('Jueves', 'Jueves'),
    ('Viernes', 'Viernes'),
    ('Sábado', 'Sábado'),
    ('Domingo', 'Domingo'),
)

category_choise = (
    ('Ejecutivo', 'Ejecutivo'),
    ('Especiales', 'Especiales'),
    ('Generales', 'Generales'),
)


class Dishes(models.Model):
    dia                = models.CharField(max_length=50, blank=False, null=True,choices=days_choise)
    categoria          = models.CharField(max_length=50, blank=False, null=True, choices=category_choise)
    descripcion        = models.TextField(max_length=255 ,blank=False, null=True) 
    precio             = models.CharField(max_length=255, blank=False, null=True) 

    def __str__(self):
        return f' Plato de dia : {self.dia} - Categoría:  {self.categoria}'


estado_envio_choise = (
    ('En Proceso', 'En Proceso'),
    ('Despachado', 'Despachado'),
    ('En Camino', 'En Camino'),
    ('Recibida', 'Recibida'),
    ('Rechazada', 'Rechazada'),

)

class Order(models.Model):
    fecha_creacion          = models.DateTimeField(default=timezone.now)
    proveedor               = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    producto                = models.CharField(max_length=50, null=True, blank=False)
    cantidad                = models.CharField(max_length=50, null=True, blank=False)
    mensaje                 = models.TextField(max_length=500 ,blank=True, null=True)
    estado                  = models.CharField(default="En Proceso", max_length=50, null=True, blank=False, choices=estado_envio_choise)

    def __str__(self):
        return f'{self.proveedor} - {self.cantidad}'
  

product_choise = (
    ('Stock Crítico', 'Stock Crítico'),
    ('No Crítico', 'No Crítico'),

)

category_choise = (
    ('Bebestibles', 'Bebestibles'),
    ('Carnes', 'Carnes'),
    ('Congelados', 'Congelados'),
    ('Lácteos', 'Lácteos'),
    ('Pastas', 'Pastas'),
    ('Verduras', 'Verduras'),
    ('No Perecibles', 'No Perecibles'),
    ('Otros', 'Otros'),

)


class Product(models.Model):
    codigo_producto         = models.CharField(max_length=80, null=True, blank=False)
    categoria               = models.CharField(max_length=50, null=True, blank=False, choices=category_choise)
    producto                = models.CharField(max_length=50, null=True, blank=False)
    descripcion             = models.TextField(max_length=255, blank=True, null=True) 
    precio                  = models.CharField(max_length=50, null=True, blank=False)
    stock                   = models.CharField(max_length=50, null=True, blank=False)
    tipo_producto           = models.CharField(max_length=50, null=True, blank=False, choices=product_choise)


    def __str__(self):
        return f'{self.producto} - {self.stock} - {self.tipo_producto}'