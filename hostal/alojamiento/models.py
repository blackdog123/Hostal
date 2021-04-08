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

    class Meta:
        ordering = ['fecha_creacion']

    def _str_(self):
        return f'{self.user.username}: {self.content}'


class Comment(models.Model):
    post                = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user                = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion      = models.DateTimeField(default=timezone.now)
    texto               = models.TextField()

    class Meta:
        ordering = ['fecha_creacion']

    def __str__(self):
        return f'{self.user.username}: comentario post_id {self.post.id}'


#----------------------------------------------------------------------#

class Profile(models.Model):
    user                    = models.OneToOneField(User, on_delete=models.CASCADE)
    bio                     = models.TextField(max_length=255, null=True, blank=True)  
    telefono                = models.CharField(max_length=9, null=True, blank=True)
    foto_perfil             = models.ImageField(default='user_default.png', upload_to='fotos_perfil')
    twitter                 = models.CharField(max_length=50, null=True, blank=True)
    instagram               = models.CharField(max_length=50, null=True, blank=True)
    facebook                = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f' perfil de {self.user.first_name}'


permissions_choice = (
    ('Solicitante', 'Solicitante'),
    ('No Solicitante ', 'No Solicitante'),
)

class Employee(models.Model):
    empresa                 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='employees')
    cargo                   = models.CharField(max_length=255, null=True, blank=True)
    nombre                  = models.CharField(max_length=255, null=True, blank=True)
    apellido                = models.CharField(max_length=255, null=True, blank=True)
    rut                     = models.CharField(max_length=9, null=True, blank=True)
    solicitante             = models.CharField(max_length=50, null=True, blank=True, choices=permissions_choice)

 
    def __str__(self):
        return f' id {self.id} - {self.nombre} {self.apellido} - {self.cargo} - {self.solicitante} '


# ignorar estos 2 modelos "estate" y "place"***************************************
class Estate(models.Model):
    estado                  = models.TextField()

class Place(models.Model):
    sede                    = models.TextField()

#*********************************************************************************        

class Number(models.Model):
    numero_habitacion       = models.TextField()

    def __str__(self):
        return f'{self.numero_habitacion}'

class Type(models.Model):
    tipo_cama               = models.TextField()

    def __str__(self):
        return f'{self.tipo_cama}'


type_room_choice = (
    ('Básico', 'Básico'),
    ('Plus', 'Plus'),
    ('Premuim', 'Premuim'),
 
)

estate_choice = (
    ('Disponible', 'Disponible'),
    ('Ocupada', 'Ocupada'),
    ('En Mantenimiento', 'En Mantenimiento'), 
)

class Room(models.Model):  
    tipo_habitacion         = models.CharField(max_length=50, null=True, blank=True, choices=type_room_choice)
    numero_habitacion       = models.ForeignKey(Number, on_delete=models.CASCADE, related_name='numbers')
    estado                  = models.CharField(max_length=50, null=True, blank=True, choices=estate_choice)
    tipo_cama               = models.ForeignKey(Type, on_delete=models.CASCADE, related_name="types")
    accesorios              = models.TextField(max_length=255, null=True, blank=True)
    precio                  = models.CharField(max_length=255, null=True, blank=True) 


    def __str__(self):
        return f'N° Habitación : {self.numero_habitacion} - {self.estado} - {self.tipo_habitacion}'



huesped_choice = (
    ('En Alojamiento', 'En Alojamiento'),
    ('Retirado', 'Retirado'),
)

noches_choice = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
 
)

class Guest(models.Model):      
    fecha_creacion          = models.DateTimeField(default=timezone.now) 
    empresa                 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enterprises')
    habitacion              = models.ForeignKey(Room, on_delete=models.CASCADE,  related_name='rooms')
    noches                  = models.CharField(max_length=50, null=True, blank=True, choices=noches_choice)
    nombre                  = models.CharField(max_length=255, null=True, blank=True) 
    apellido                = models.CharField(max_length=255, null=True, blank=True) 
    rut                     = models.CharField(max_length=9, null=True, blank=True)  
    email                   = models.CharField(max_length=255, null=True, blank=True) 
    estado_huesped          = models.CharField(max_length=50, null=True, blank=True, choices=huesped_choice)

    def __str__(self):
        return f'{self.habitacion} - {self.empresa} - {self.estado_huesped}'

noches_choice = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
 
)

personas_choise = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
)


solicitud_choise = (
    ('En Revision', 'En Revision'),
    ('Aceptada', 'Aceptada'),
    ('Rechazada', 'Rechazada'),
)


class Booking_Client(models.Model):
    user                    = models.ForeignKey(User, on_delete=models.CASCADE, related_name='booking_clients')
    fecha                   = models.DateField(null=True, blank=True)
    fecha_creacion          = models.DateTimeField(default=timezone.now)
    tipo_habitacion         = models.CharField(max_length=50, null=True, blank=True, choices=type_room_choice)
    noches                  = models.CharField(max_length=50, null=True, blank=True, choices=noches_choice)
    personas                = models.CharField(max_length=50, null=True, blank=True, choices=personas_choise)
    lista_personas          = models.TextField()
    estado                  = models.CharField(max_length=50,default="En Revision" ,null=True, blank=True, choices=solicitud_choise)

    def __str__(self):
        return f'Reserva de : {self.user.username}'
    
    def get_absolute_url(self):
        return reverse('mis_reservas')

class Ticket(models.Model):
    fecha_creacion          = models.DateTimeField(default=timezone.now)
    fecha_boleta            = models.DateField(null=True, blank=True)
    tipo_habitacion         = models.CharField(max_length=50, null=True, blank=True, choices=type_room_choice)
    precio_servivcio        = models.CharField(max_length=50, null=True, blank=True)
    noches                  = models.CharField(max_length=50, null=True, blank=True, choices=noches_choice)
    precio_noches           = models.CharField(max_length=50, null=True, blank=True)
    personas                = models.CharField(max_length=50, null=True, blank=True, choices=personas_choise)
    precio_personas         = models.CharField(max_length=50, null=True, blank=True)
    total                   = models.CharField(max_length=50, null=True, blank=True)
    from_user               = models.ForeignKey(User, default="1", related_name='user1', on_delete=models.CASCADE)
    to_user                 = models.ForeignKey(User, related_name='tickets', on_delete=models.CASCADE)

    def __str__(self):
        return f' Factura {self.from_user} a {self.to_user}'



class Proovider(models.Model):
    fecha_creacion          = models.DateTimeField(default=timezone.now)
    rubro                   = models.CharField(max_length=80, null=True, blank=True)
    rut                     = models.CharField(max_length=9, null=True, blank=True)   
    email                   = models.CharField(max_length=80, null=True, blank=True)
    telefono                = models.CharField(max_length=9, null=True, blank=True)

    def __str__(self):
        return f' Proveedor : {self.rubro}'


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
    dia                = models.CharField(max_length=50, null=True, blank=True, choices=days_choise)
    categoria          = models.CharField(max_length=50, null=True, blank=True, choices=category_choise)
    descripcion        = models.TextField() 
    precio             = models.CharField(max_length=255, null=True, blank=True) 

    def __str__(self):
        return f' Plato de dia : {self.dia} - Categoría:  {self.categoria}'