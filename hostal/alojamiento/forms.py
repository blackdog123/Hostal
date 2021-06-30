from django import forms
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from django.db.models import fields

from django.forms import ModelForm, widgets
from .models import *

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, help_text='Last Name')
    email = forms.EmailField(max_length=150, help_text='Email')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'password1', 'password2',)


class EditarUsuario(ModelForm):

    username           = forms.CharField(help_text='', label='Nombre de Usuario', widget=forms.TextInput(attrs={'readonly':'readonly'}))
    first_name         = forms.CharField(help_text='', label='Nombre de Empresa' ,widget=forms.TextInput(attrs={'readonly':'readonly'}))
    email              = forms.CharField(help_text='', label='Email' ,widget=forms.TextInput(attrs={'type':'email','readonly':'readonly'}))
    is_active          = forms.CharField(label="Activo", widget=forms.CheckboxInput(attrs={}))

    class Meta:
        model = User 
        fields = ('username', 'first_name', 'email', 'is_active',)


class EditarPermiso(ModelForm):

    class Meta:
        model = Profile
        fields = ('tipo_permiso', )


class EditarPerfil(ModelForm):

    class Meta:
        model = Profile
        fields = ('foto_perfil','foto_portada' ,'bio', 'telefono', 'twitter', 'facebook', 'instagram',)

        widgets = {
            'foto_perfil':       forms.FileInput(),
            'foto_portada':      forms.FileInput(),
            'bio':               forms.Textarea(attrs={'rows':2, 'placeholder':'Escribe alúna descripción sobre tu empresa'}),
        }


class CrearHabitacion(ModelForm):
    accesorios          = forms.CharField(label="Accesorios", widget=forms.Textarea(attrs={'rows':4,'placeholder':'Escribe algúna descripción sobre esta habitación'}))

    class Meta:
        model = Room
        fields = ('tipo_habitacion', 'numero_habitacion', 'estado','tipo_cama', 'cantidad_camas', 'cantidad_personas', 'accesorios','imagen_habitacion', 'precio', )

        widgets = {
            'numero_habitacion' :      forms.TextInput(attrs={'type':'number', 'min':0 }),
            'cantidad_camas' :      forms.TextInput(attrs={'type':'number', 'min':0 }),
            'cantidad_personas' :      forms.TextInput(attrs={'type':'number', 'min':0 }),
            'precio' :      forms.TextInput(attrs={'type':'number', 'min':0  }),
        }


class EditarHabitacion(ModelForm):

    accesorios          = forms.CharField(label="Accesorios", widget=forms.Textarea(attrs={'rows':4,'placeholder':'Escribe algúna descripción sobre esta habitación'}))
 

    class Meta:
        model = Room
        fields = ('tipo_habitacion', 'numero_habitacion', 'estado','tipo_cama', 'cantidad_camas', 'cantidad_personas', 'accesorios','imagen_habitacion', 'precio', )

        widgets = {
            'numero_habitacion' :      forms.TextInput(attrs={'type':'number', 'min':0 }),
            'cantidad_camas' :      forms.TextInput(attrs={'type':'number', 'min':0 }),
            'cantidad_personas' :      forms.TextInput(attrs={'type':'number', 'min':0 }),
            'precio' :      forms.TextInput(attrs={'type':'number', 'min':0  }),
        }



class EditarTrabajador(ModelForm):
 
    class Meta:
        model = Employee
        fields = ('nombre','apellido', 'rut', 'cargo',)

        widgets = {
            'nombre' :         forms.TextInput(attrs={'placeholder':'Nombre del Empleado'}),
            'apellido' :       forms.TextInput(attrs={'placeholder':'Apellido del Empleado'}),
            'rut' :            forms.TextInput(attrs={'placeholder':'Ej: 111111111', 'max_length':'9'}),
        }


class EditarInfo(UserChangeForm):

    username =        forms.CharField(label="Nombre Usuario")
    first_name =      forms.CharField(label="Nombre Empresa")
    email =           forms.CharField(label="Email")
    
    class Meta:
        model = User
        fields = ('username','first_name', 'email', 'password',)



class PasswordChangingForm(PasswordChangeForm):

    old_password =       forms.CharField(label='Contraseña Actual', widget=forms.PasswordInput(attrs={'type':'password'}))
    new_password1 =      forms.CharField(label='Nueva Contraseña', widget=forms.PasswordInput(attrs={'type':'password'}))
    new_password2 =      forms.CharField(label='Confirmar Nueva Contraseña', widget=forms.PasswordInput(attrs={'type':'password'}))
    
    class Meta:
        model = User
        fields = ('old_password','new_password1', 'new_password2',)

class EditarInfoProveedor(ModelForm):

    username =        forms.CharField(label="Nombre Usuario")
    email =           forms.CharField(label="Email")
    
    class Meta:
        model = User
        fields = ('username', 'email',)


class VerReservacion(ModelForm):

    class Meta:
        model = Booking_Client
        fields = ('estado',) 

        
class CrearFactura(ModelForm):

    class Meta:
        model = Ticket
        fields = ('fecha_boleta','habitacion_reservada','precio_servicio', 'cantidad_dias', 'precio_dias', 'subtotal', 'iva', 'total', 'receptor')

        widgets = {
            
            'fecha_boleta':             forms.TextInput(attrs={'type':'date'}),
            'precio_servicio':          forms.TextInput(attrs={'type':'number','min':0, 'placeholder': '0','id':'txt_campo_1','class':'monto', 'onkeyup':'sumar()'}),
            'cantidad_dias':            forms.TextInput(attrs={'type':'number','min':0,}),
            'precio_dias':              forms.TextInput(attrs={'type':'number','min':0, 'placeholder': '0', 'id':'txt_campo_2','class':'monto' , 'onkeyup':'sumar()'}),      
            'subtotal':                 forms.TextInput(attrs={'id':'spTotal', 'readonly':'readonly'}),         
            'iva':                      forms.TextInput(attrs={'name':'iva', 'readonly':'readonly'}),
            'total':                    forms.TextInput(attrs={'name':'total', 'readonly':'readonly'})

        }

class EditarFactura(ModelForm):

     class Meta:
        model = Ticket
        fields = ('fecha_boleta', 'habitacion_reservada','precio_servicio', 'cantidad_dias', 'precio_dias', 'subtotal', 'iva', 'total', 'estado_ticket')

        widgets = {
          
            'fecha_boleta':             forms.TextInput(attrs={'type':'date', 'readonly':'readonly' }),
            'habitacion_reservada':     forms.TextInput(attrs={'type':'select','readonly':'readonly'}),
            'precio_servicio':          forms.TextInput(attrs={'id':'txt_campo_1','class':'monto' , 'onkeyup':'sumar()','readonly':'readonly'}),
            'cantidad_dias':            forms.TextInput(attrs={'readonly':'readonly'}),
            'precio_dias':              forms.TextInput(attrs={'readonly':'readonly'}), 
            'subtotal':                 forms.TextInput(attrs={'readonly':'readonly'}),    
            'iva':                      forms.TextInput(attrs={'readonly':'readonly'}),
            'total':                    forms.TextInput(attrs={'id':'spTotal', 'readonly':'readonly'}),
        }


class NuevoHesped(ModelForm):
    nombre = forms.CharField(label='Nombre', widget=forms.TextInput(attrs={'placeholder':'nombre huésped'}))
    apellido = forms.CharField(label='Apellido', widget=forms.TextInput(attrs={'placeholder':'apellido huésped'}))
    rut = forms.CharField(label='Rut', widget=forms.TextInput(attrs={'placeholder':'Ej: 111111111', 'maxlength':9 }))
  


    class Meta:
        model = Guest
        fields = ('empresa', 'habitacion', 'fecha_ingreso','fecha_salida', 'nombre', 'apellido', 'rut', ) 

    
        widgets = {
            'fecha_ingreso':     forms.TextInput(attrs={'type':'date'}),
            'fecha_salida':      forms.TextInput(attrs={'type':'date'}),
        }

class EditarHuesped(ModelForm):

    nombre = forms.CharField(label='Nombre', widget=forms.TextInput(attrs={'placeholder':'nombre huésped'}))
    apellido = forms.CharField(label='Apellido', widget=forms.TextInput(attrs={'placeholder':'apellido huésped'}))
    rut = forms.CharField(label='Rut', widget=forms.TextInput(attrs={'placeholder':'Ej: 111111111', 'maxlength':9 }))
   
    class Meta:
        model = Guest
        fields = ('empresa', 'habitacion', 'fecha_ingreso','fecha_salida', 'nombre', 'apellido', 'rut', 'estado_huesped')


        widgets = {
            'fecha_ingreso':     forms.TextInput(attrs={'type':'date'}),
            'fecha_salida':      forms.TextInput(attrs={'type':'date'}),
        }


    
class NuevoProveedor(ModelForm):

    class Meta:
        model = Proovider
        fields = ('empresa', 'rubro', )

        widgets = {
     
            'rubro' :               forms.TextInput(attrs={'placeholder':'Rubro empresa o proveedor'}),  
        }

class EditarPorveedor(ModelForm):

    class Meta:
        model = Proovider
        fields = ('empresa', 'rubro', )
    
        widgets = {
  
            'rubro' :               forms.TextInput(attrs={'placeholder':'Rubro empresa o proveedor'}),    
        }

class CrearPlato(ModelForm):

    class Meta:
        model = Dishes
        fields = ('dia', 'categoria', 'descripcion', 'precio')

        widgets = {
            'descripcion' :     forms.Textarea(attrs={'rows':'3' ,'placeholder':'Describe aquí el plato'}),
            'precio' :          forms.NumberInput(attrs={'placeholder':'precio del plato', 'min':0 }),
        }

class EditarPlato(ModelForm):

    class Meta:
        model = Dishes
        fields = ('dia', 'categoria', 'descripcion', 'precio')

        widgets = {
            'descripcion' :     forms.Textarea(attrs={'rows':'3' ,'placeholder':'Describe aquí el plato'}),
            'precio' :          forms.NumberInput(attrs={'placeholder':'precio del plato', 'min':0 }),
        }


class NuevoEmpleado(ModelForm):

    class Meta:
        model = Employee
        fields = ('nombre', 'apellido', 'rut', 'cargo',)

        widgets = {
            'nombre' :         forms.TextInput(attrs={'placeholder':'Nombre del Empleado'}),
            'apellido' :       forms.TextInput(attrs={'placeholder':'Apellido del Empleado'}),
            'rut' :            forms.TextInput(attrs={'placeholder':'Ej: 111111111', 'max_length':'9'}),
        }


class NuevoPedido(ModelForm):
    
    class Meta:
        model  = Order
        fields = ('proveedor', 'producto','cantidad', 'mensaje',)


        widgets = {
            'cantidad' :            forms.NumberInput(attrs={'placeholder':'Ingresa la cantidad del producto a pedir', 'min':0}),
            'mensaje':              forms.Textarea(attrs={'rows':3, 'placeholder':'Escribe algún mensaje al proveedor'}),
        }

class EditarPedido(ModelForm):

    class Meta:
        model  = Order
        fields = ('proveedor', 'producto','cantidad', 'mensaje',)

        widgets = {
            'cantidad' :            forms.NumberInput(attrs={'min':0}),
            'mensaje':              forms.Textarea(attrs={'rows':3, 'placeholder':'Escribe algún mensaje al proveedor'}),
        }

estado_envio_choise = (
    ('En Proceso', 'En Proceso'),
    ('Despachado', 'Despachado'),
    ('En Camino', 'En Camino'),
    ('Recibida', 'Recibida'),
    ('Rechazada', 'Rechazada'),

)

class EstadoOrden(ModelForm):
    estado          = forms.ChoiceField(label="", choices=estado_envio_choise)

    class Meta:
        model = Order
        fields = ('estado',)


class NuevoProducto(ModelForm):

    class Meta:
        model = Product
        fields = ('codigo_producto', 'categoria', 'producto', 'descripcion', 'precio', 'stock', 'tipo_producto')

        widgets = {
        'codigo_producto' : forms.NumberInput(attrs={'placeholder':'código del producto', 'min':0 }),
        'producto' :            forms.TextInput(attrs={'placeholder':'Nombre del producto'}),
        'descripcion':      forms.Textarea(attrs={'rows':3, 'placeholder':'Escribe algúnna descripción del producto'}),
        'precio' :          forms.NumberInput(attrs={'placeholder':'precio del producto', 'min':0 }),
        'stock' :          forms.NumberInput(attrs={'placeholder':'cantidad de stock', 'min':0 }),
        }


class EditarProducto(ModelForm):
    descripcion          = forms.CharField(label="Descripción", widget=forms.Textarea(attrs={'rows':3,'placeholder':'Escribe algúna descripción sobre este producto'}))

    class Meta:
        model = Product
        fields = ('codigo_producto', 'categoria', 'producto', 'descripcion', 'precio', 'stock', 'tipo_producto')
        
        widgets = {
        'codigo_producto' : forms.NumberInput(attrs={'placeholder':'código del producto', 'min':0 }),
        'producto' :            forms.TextInput(attrs={'placeholder':'Nombre del producto'}),
        'descripcion':      forms.Textarea(attrs={'rows':3, 'placeholder':'Escribe algúnna descripción del producto'}),
        'precio' :          forms.NumberInput(attrs={'placeholder':'precio del producto', 'min':0 }),
        'stock' :          forms.NumberInput(attrs={'placeholder':'cantidad de stock', 'min':0 , 'readonly':'readonly'}),
        }


class AgregarStock(ModelForm):
   
    class Meta:
        model = Product
        fields = ('producto', 'descripcion', 'stock', )
        
        widgets = {
        'producto' :            forms.TextInput(attrs={'placeholder':'Nombre del producto' , 'readonly':'readonly'}),
        'descripcion':      forms.Textarea(attrs={'rows':3, 'placeholder':'Escribe algúnna descripción del producto', 'readonly':'readonly'}),
        'stock' :          forms.NumberInput(attrs={'placeholder':'cantidad de stock', 'min':0 , 'readonly':'readonly', 'id':'spTotal'}),
        }


class OcuparStock(ModelForm):
   
    class Meta:
        model = Product
        fields = ('producto', 'descripcion', 'stock', )
        
        widgets = {
        'producto' :            forms.TextInput(attrs={'placeholder':'Nombre del producto' , 'readonly':'readonly'}),
        'descripcion':      forms.Textarea(attrs={'rows':3, 'placeholder':'Escribe algúna descripción del producto', 'readonly':'readonly'}),
        'stock' :          forms.NumberInput(attrs={'placeholder':'cantidad de stock', 'min':0 , 'readonly':'readonly', 'id':'spTotal'}),
        }


class EditarPost(ModelForm):

    class Meta: 
        model = Post
        fields = ('Titulo',)

        widgets = {
        'Titulo':      forms.Textarea(attrs={'rows':3, 'placeholder':'Escribe algún títilo para tu publicación'}),
 
        }