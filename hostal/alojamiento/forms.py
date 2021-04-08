from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.forms import ModelForm, widgets
from .models import *

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, help_text='Last Name')
    email = forms.EmailField(max_length=150, help_text='Email')

    class Meta:
        model = User
        fields = ('username', 'first_name',
'email', 'password1', 'password2',)


class EditarPerfil(ModelForm):
    foto_perfil = forms.ImageField(label="Foto de Perfil ", widget=forms.FileInput(attrs={}))
    bio = forms.CharField(label="Descripción ", widget=forms.Textarea(attrs={'rows':4,'placeholder':'Escribe algúna descripción o algo sobre tú Empresa'}))
    telefono = forms.CharField(label="Teléfono",max_length="9",widget=forms.TextInput(attrs={'placeholder': 'Ej: 123456789'}))
   

    class Meta:
        model = Profile
        fields = ('foto_perfil','bio','telefono', 'twitter', 'facebook', 'instagram',)



class CrearHabitacion(ModelForm):
    accesorios          = forms.CharField(label="Accesorios", widget=forms.Textarea(attrs={'rows':4,'placeholder':'Escribe algúna descripción sobre esta habitación'}))

    class Meta:
        model = Room
        fields = ('tipo_habitacion', 'numero_habitacion', 'estado', 'tipo_cama', 'accesorios', 'precio',)


class EditarHabitacion(ModelForm):

    accesorios          = forms.CharField(label="Accesorios", widget=forms.Textarea(attrs={'rows':4,'placeholder':'Escribe algúna descripción sobre esta habitación'}))
 

    class Meta:
        model = Room
        fields = ('tipo_habitacion', 'numero_habitacion', 'estado','tipo_cama', 'accesorios', 'precio', )


class EditarTrabajador(ModelForm):
    nombre   = forms.CharField(label="Nombre")
    apellido = forms.CharField(label="Apellido")
    email    = forms.CharField(label="Email")
    rut      = forms.CharField(label="Rut sin puntos ni guión",max_length=9, widget=forms.TextInput(attrs={'size':9,'max':999999999, 'min':0, 'placeholder': 'Ej: 111111111 '}))
    telefono = forms.CharField(label="Teléfono", widget=forms.NumberInput(attrs={'size':9,'max':999999999, 'min':0, 'placeholder': 'Ej: 123456789 '}))

    class Meta:
        model = Employee
        fields = ('nombre','apellido', 'email','rut', 'telefono',)


class ReservarForm(ModelForm):

    class Meta:
        model = Booking_Client
        fields = ('user','fecha', 'tipo_habitacion', 'noches', 'personas', 'lista_personas',)

        widgets = {
            'user':  forms.TextInput(attrs={'value':'', 'id':'elder', 'type':'hidden'}),
            'fecha': forms.TextInput(attrs={'type':'date'}),
            'lista_personas': forms.Textarea(attrs={'rows':4, 'placeholder':'Escribe aquí los "ID" o el Nombre de los trabajadores al que se le realizará la reserva ', }),
        }


class EditarInfo(ModelForm):

    username =        forms.CharField(label="Nombre Usuario")
    first_name =      forms.CharField(label="Nombre Empresa")
    email =           forms.CharField(label="Email")
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email',)


class VerReservacion(ModelForm):

    class Meta:
        model = Booking_Client
        fields = ('user', 'fecha', 'tipo_habitacion', 'noches', 'personas', 'lista_personas', 'estado') 

        widgets = {
            'user':                     forms.TextInput(attrs={'type':'hidden','readonly':'readonly', 'value':'user.username'}),
            'fecha':                    forms.TextInput(attrs={'type':'date','readonly':'readonly'}),
            'tipo_habitacion':          forms.TextInput(attrs={'readonly':'readonly'}),
            'noches':                   forms.TextInput(attrs={'readonly':'readonly'}),
            'personas':                 forms.TextInput(attrs={'readonly':'readonly'}),
            'lista_personas':           forms.Textarea(attrs={'rows':2,'readonly':'readonly'}),
        }

class CrearFactura(ModelForm):

    class Meta:
        model = Ticket
        fields = ('fecha_boleta', 'tipo_habitacion', 'precio_servivcio', 'noches', 'precio_noches', 'personas', 'precio_personas', 'total', 'from_user', 'to_user',)

        widgets = {
            'from_user':                forms.TextInput(attrs={'readonly':'readonly', 'type':'hidden'}),
            'fecha_boleta':             forms.TextInput(attrs={'type':'date'}),
            'precio_servivcio':         forms.TextInput(attrs={'id':'txt_campo_1', 'class':'monto' , 'onkeyup':'sumar()'}),
            'precio_noches':            forms.TextInput(attrs={'id':'txt_campo_2', 'class':'monto' , 'onkeyup':'sumar()'}),
            'precio_personas':          forms.TextInput(attrs={'id':'txt_campo_3', 'class':'monto' , 'onkeyup':'sumar()'}),
            'total':                    forms.TextInput(attrs={'id':'spTotal', 'readonly':'readonly'})

        }


class NuevoHesped(ModelForm):

    class Meta:
        model = Guest
        fields = ('empresa', 'habitacion', 'noches', 'nombre', 'apellido', 'rut', 'email', 'estado_huesped') 

class EditarHuesped(ModelForm):

    class Meta:
        model = Guest
        fields = ('empresa', 'habitacion', 'noches', 'nombre', 'apellido', 'rut', 'email', 'estado_huesped')


class NuevoProveedor(ModelForm):

    class Meta:
        model = Proovider
        fields = ('rubro','rut', 'email', 'telefono',)

        widgets = {
            'rubro' :           forms.TextInput(attrs={'placeholder':'Rubro del vendedor'}),
            'rut' :             forms.TextInput(attrs={'type':'text' ,'placeholder':'Ej: 111111111'}),
            'email' :           forms.TextInput(attrs={'type':'email' ,'placeholder':'Email'}),
            'telefono' :        forms.TextInput(attrs={'type':'number', 'max_length':'9', 'min':'0','max':'99999999' ,'placeholder':'Teléfono'}),
        }

class EditarPorveedor(ModelForm):

    class Meta:
        model = Proovider
        fields = ('rubro','rut', 'email', 'telefono',)
    
        widgets = {
            'rubro' :           forms.TextInput(attrs={'placeholder':'Rubro del vendedor'}),
            'rut' :             forms.TextInput(attrs={'type':'text' ,'placeholder':'Ej: 111111111'}),
            'email' :           forms.TextInput(attrs={'type':'email' ,'placeholder':'Email'}),
            'telefono' :        forms.TextInput(attrs={'type':'number', 'max_length':'9', 'min':'0','max':'99999999' ,'placeholder':'Teléfono'}),
        }

class CrearPlato(ModelForm):

    class Meta:
        model = Dishes
        fields = ('dia', 'categoria', 'descripcion', 'precio')

        widgets = {
            'descripcion' :     forms.Textarea(attrs={'rows':'3' ,'placeholder':'Describe aquí el plato'}),
            'precio' :          forms.TextInput(attrs={'placeholder':'precio del plato'}),
        }

class EditarPlato(ModelForm):

    class Meta:
        model = Dishes
        fields = ('dia', 'categoria', 'descripcion', 'precio')

        widgets = {
            'descripcion' :     forms.Textarea(attrs={'rows':'3' ,'placeholder':'Describe aquí el plato'}),
            'precio' :          forms.TextInput(attrs={'placeholder':'precio del plato'}),
        }

        