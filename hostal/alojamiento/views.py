from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
import time
from .models import *
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from .forms import SignUpForm, CrearHabitacion, EditarHabitacion, EditarPerfil, EditarTrabajador, ReservarForm, EditarInfo,VerReservacion, CrearFactura, NuevoHesped, EditarHuesped, NuevoProveedor, EditarPorveedor, CrearPlato, EditarPlato
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .filters import RoomFilter, GuestFilter, BookingFilter, TicketFilter, ProviderFilter, DishesFilter
from django.contrib.auth.decorators import login_required


# Create your views here.

#-------------------------- vistas opiniones, reserva_cliente e index -------------------------
class Homeview(ListView):
    model = Post
    template_name = 'index.html'

class Opiniones(DetailView):
    model = Post
    template_name = 'opiniones.html'


def publicar_comentario(request, pk):
    if request.user.is_authenticated:
        if request.method == "POST":
            mi_post = request.POST['post_id']
            mi_user = request.POST['user_id']
            mi_texto = request.POST['texto']
            
            if mi_post != "" or mi_user != "" or mi_texto != "":
                try:
                    
                    comment = Comment()

                    comment.post_id  = mi_post 
                    comment.user_id  = mi_user 
                    comment.texto = mi_texto
                    comment.activo = 1

                    comment.save()
                
                    return HttpResponseRedirect(reverse('opiniones', args=[str(pk)]))
                    
                except comment.DoesNotExist:
                    messages.error(request, 'Tú comentario no se pudo publicar, por favor intententalo nuevamente')
                    return HttpResponseRedirect(reverse('opiniones', args=[str(pk)]))
            
            else:
                messages.error(request, 'lo sentimos, tú comentario no se pudo publicar, por favor intententalo nuevamente ')
                return HttpResponseRedirect(reverse('opiniones', args=[str(pk)]))
        
        else:
            messages.error(request, 'El metodo post es incorrecto ')
            return HttpResponseRedirect(reverse('opiniones', args=[str(pk)]))
    
    else: 
        return redirect('/login')   

class ReservaView(LoginRequiredMixin, CreateView):
    model = Booking_Client
    template_name = 'reservar.html'
    form_class = ReservarForm

    login_url = '/login'


def mis_reservas(request, username=None):
    if request.user.is_authenticated:
        
        current_user = request.user
        if username and username != current_user.username:
            user = User.objects.get(username=username)
            booking_clients = user.booking_clients.all()
        else:
            booking_clients = current_user.booking_clients.all().order_by('-fecha_creacion')
            user = current_user

        return render(request, 'mis_reservas.html', {'user':user, 'booking_clients':booking_clients})

    else: 
        return redirect('/login')


def mis_facturas(request, username=None):
    if request.user.is_authenticated:
        
        current_user = request.user
        if username and username != current_user.username:
            user = User.objects.get(username=username)
            tickets = user.tickets.all()
        else:
            tickets = current_user.tickets.all()
            user = current_user

        return render(request, 'mis_facturas.html', {'user':user, 'tickets':tickets})

    else: 
        return redirect('/login')


def perfil(request, username=None):
    if request.user.is_authenticated:

        current_user = request.user
        if username and username != current_user.username:
            user = User.objects.get(username=username)
            employees = user.employees.all()
        else:
            employees = current_user.employees.all()
            user = current_user

        return render(request, 'perfil.html', {'user':user, 'employees':employees})

    else:
        return redirect('/login')



@login_required(login_url='/login')
def configuracion(request, id):
    instancia = User.objects.get(id=id)
    form = EditarInfo(instance=instancia)

    if request.method == "POST":
     
        form = EditarInfo(request.POST,request.FILES, instance=instancia)

        if form.is_valid():
    
            instancia = form.save(commit=False)
     
            instancia.save()

            messages.success(request, 'Se editó tú información')
            return redirect('/perfil')

        else:

            messages.error(request, 'No se pudo Editar tú Información, por favor intentalo nuevamente')
            return redirect('/editar_perfil')


    return render(request, "configuracion.html", {'form': form})

#-----------------------------------------------logIn, signup and logout-------------------------------------------  

def login(request):
    form = AuthenticationForm()
    if request.method == "POST":

        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                do_login(request, user)

            return redirect('/')
        else:
            messages.error(request, "Verifique Bien su Usuario y Contraseña")
            return redirect('/login')
            
    return render(request, "login.html", {'form': form})

def logout(request):
    if request.user.is_authenticated:
        do_logout(request)
        return redirect('/')
    else:
        return redirect('/')

def registro(request):
    form = SignUpForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data.get('first_name')
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            do_login(request, user)
            messages.success(request, f'Bienvenido {username}')
            return redirect('/')
        else:
            messages.error(request, "No se pudo crear el usuario Correctamente, puede que ya exista alguien con ese nombre de usuario, o la contraseña es muy debíl, por favor intentalo nuevamente")
            return redirect('/registro')

    form = SignUpForm()
    return render(request, 'registro.html', {'form': form})


def login_empleados(request):
    form = AuthenticationForm()
    if request.method == "POST":

        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                do_login(request, user)

            return redirect('/proveedores')
        else:
            messages.error(request, "Verifique Bien su Usuario y Contraseña")
            return redirect('/login_empleados')
            
    return render(request, "login_empleados.html", {'form': form})
 
#------------------------------------------------ vistas perfil -------------------------------------------------


def perfil(request, username=None):
    if request.user.is_authenticated:

        current_user = request.user
        if username and username != current_user.username:
            user = User.objects.get(username=username)
            employees = user.employees.all()
        else:
            employees = current_user.employees.all()
            user = current_user

        return render(request, 'perfil.html', {'user':user, 'employees':employees})

    else:
        return redirect('/login')


@login_required(login_url='/login')
def editar_perfil(request, user_id):
    instancia = Profile.objects.get(user=user_id)
    form = EditarPerfil(instance=instancia)

    if request.method == "POST":
     
        form = EditarPerfil(request.POST,request.FILES, instance=instancia)

        if form.is_valid():
    
            instancia = form.save(commit=False)
     
            instancia.save()

            messages.success(request, 'Se Editó Tu Perfil')
            return redirect('/perfil')

        else:

            messages.error(request, 'No se pudo Editar tu Perfil, por favor intentalo nuevamente')
            return redirect('/editar_perfil')


    return render(request, "editar_perfil.html", {'form': form})

#----------------------------------- vistas agregar trabajador de empresa -----------------------------------
    #if request.user.is_authenticated:
    #    return render(request, 'agregar_trabajador.html')
    #else: 
    #    return redirect('/login')

    
def guardar_trabajador(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            mi_empresa = request.POST['empresa_id']
            mi_nombre = request.POST['nombre']
            mi_apellido = request.POST['apellido']
            mi_email = request.POST['email']
            mi_telefono = request.POST['telefono']
            mi_rut = request.POST['rut']
            
            if mi_empresa != "" or mi_nombre != "" or mi_apellido != "" or mi_rut:

                try:
                    
                    employee = Employee()

                    employee.empresa_id  = mi_empresa
                    employee.nombre = mi_nombre
                    employee.apellido = mi_apellido
                    employee.email = mi_email
                    employee.telefono = mi_telefono
                    employee.rut = mi_rut
                 
                    employee.save()
                    
                    messages.success(request, 'Tú trabajador se guardo correctamente')
                    return redirect( '/perfil')
                    
                
                except employee.DoesNotExist:
                    messages.error(request, 'Tú Trabajador no pudo guardar correctamente, por favor intetalo nuevamente')
                    return redirect(request, '/agregar_trabajador')
            
            else:
                messages.error(request, 'Tú Trabajador no pudo guardar correctamente, por favor intetalo nuevamente')
                return redirect(request, '/agregar_trabajador')
        
        else:
            messages.error(request, 'El método post no es correcto ')
            return redirect(request, '/agregar_trabajador')
    
    else: 
        return redirect('/login')  


@login_required(login_url='/login')
def editar_trabajador(request, id):
    instancia = Employee.objects.get(id=id)
    form = EditarTrabajador(instance=instancia)

    if request.method == "POST":
     
        form = EditarTrabajador(request.POST, instance=instancia)

        if form.is_valid():
    
            instancia = form.save(commit=False)
     
            instancia.save()

            messages.success(request, 'Se editó a tú trabajador')
            return redirect('/perfil')

        else:

            messages.error(request, 'No se pudo editar tú trabajador, por favor intentalo nuevamente')
            return redirect('/editar_trabajador')


    return render(request, "editar_trabajador.html", {'form': form})

def eliminar_trabajador(request, id):
    instancia = Employee.objects.get(id=id)
    instancia.delete()

    messages.success(request, 'Se eliminó a tú trabajador')
    return redirect('/perfil')



#------------------------------------------------ vistas administración --------------------------------

class DashboardView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'dashboard.html'

    login_url = '/login'
 

def habitaciones(request):
    if request.user.is_authenticated:
        room_list = Room.objects.all()
        user_filter = RoomFilter(request.GET, queryset=room_list)
        return render(request, 'habitaciones.html', {'filter': user_filter})
    else:
        return redirect('/login')


@login_required(login_url='/login')
def crear_habitacion(request):
    form = CrearHabitacion(request.POST)
    if request.method == "POST":

        if form.is_valid():
            form.save()
            numero_habitacion = form.cleaned_data.get('numero_habitacion')
            estado = form.cleaned_data.get('estado')
            tipo_cama = form.cleaned_data.get('tipo_cama')
            accesorios = form.cleaned_data.get('accesorios')
            precio = form.cleaned_data.get('precio')
            foto_habitacion = form.cleaned_data.get('foto_habitacion')
            
            messages.success(request, "La habitación se creó correctamente")
            return redirect('/habitaciones')
        else:
            messages.error(request, "No de pudo crear la habitación correctamente, por favor intentalo nuevamente")
            return redirect('/crear_habitacion')

    form = CrearHabitacion()
    return render(request, 'crear_habitacion.html', {'form':form})


@login_required(login_url='/login')   
def editar_habitacion(request, id):

    instancia = Room.objects.get(id=id)
    form = EditarHabitacion(instance=instancia)

    if request.method == "POST":
     
        form = EditarHabitacion(request.POST, instance=instancia)

        if form.is_valid():
    
            instancia = form.save(commit=False)
     
            instancia.save()

            messages.success(request, 'Se Editó la Habitación')
            return redirect('/habitaciones')

        else:

            messages.error(request, 'No se pudo Editar la Habitación, por favor intentalo nuevamente')
            return redirect(request, '/editar_habitacion')


    return render(request, "editar_habitacion.html", {'form': form})

    
@login_required(login_url='/login')
def eliminar_habitacion(request, id):
    if request.user.is_authenticated:
        instancia = Room.objects.get(id=id)
        instancia.delete()

        messages.success(request, 'Se Eliminó la Habitación')
        return redirect('/habitaciones')
    else:
        return redirect('/login')

#------------------------------------------------ vistas platos/minuta semanal --------------------------------

def comedor(request):
    if request.user.is_authenticated:
        dishes_list = Dishes.objects.all()
        user_filter = DishesFilter(request.GET, queryset=dishes_list)
        return render(request, 'comedor.html', {'filter': user_filter})
    else:
        return redirect('/login')


@login_required(login_url='/login')
def nuevo_plato(request):
    form = CrearPlato(request.POST)
    if request.method == "POST":

        if form.is_valid():
            form.save()
            dia = form.cleaned_data.get('dia')
            categoria = form.cleaned_data.get('categoria')
            descripcion = form.cleaned_data.get('descripcion')
            precio = form.cleaned_data.get('precio')
            
            messages.success(request, "El plato se creó correctamente")
            return redirect('/comedor')
        else:
            messages.error(request, "No de pudo crear El plato correctamente, por favor intentalo nuevamente")
            return redirect('/nuevo_plato')

    form = CrearPlato()
    return render(request, 'nuevo_plato.html', {'form':form})


@login_required(login_url='/login')   
def editar_plato(request, id):

    instancia = Dishes.objects.get(id=id)
    form = EditarPlato(instance=instancia)

    if request.method == "POST":
     
        form = EditarPlato(request.POST, instance=instancia)

        if form.is_valid():
    
            instancia = form.save(commit=False)
     
            instancia.save()

            messages.success(request, 'Se Editó el plato')
            return redirect('/comedor')

        else:

            messages.error(request, 'No se pudo editar el plato, por favor intentalo nuevamente')
            return redirect(request, '/editar_plato')


    return render(request, "editar_plato.html", {'form': form})


@login_required(login_url='/login')
def eliminar_plato(request, id):
    if request.user.is_authenticated:
        instancia = Dishes.objects.get(id=id)
        instancia.delete()

        messages.success(request, 'Se Eliminó el plato')
        return redirect('/comedor')
    else:
        return redirect('/login')

#------------------------------------------------- vistas huespedes -------------------------------------------------

def huespedes(request):
    if request.user.is_authenticated:
        guest_list = Guest.objects.all()
        user_filter = GuestFilter(request.GET, queryset=guest_list)
        return render(request, 'huespedes.html', {'filter': user_filter})
    else:
        return redirect('/login')


@login_required(login_url='/login')
def nuevo_huesped(request):
    form = NuevoHesped(request.POST)
    if request.method == "POST":

        if form.is_valid():
            form.save()
            empresa = form.cleaned_data.get('empresa')
            habitacion = form.cleaned_data.get('habitacion')
            noches = form.cleaned_data.get('noches')
            nombre = form.cleaned_data.get('nombre')
            apellido = form.cleaned_data.get('apellido')
            rut = form.cleaned_data.get('rut')
            email = form.cleaned_data.get('email')
            estado = form.cleaned_data.get('estado')

            
            messages.success(request, "El huésped se registró correctamente")
            return redirect('/huespedes')
        else:
            messages.error(request, "No de pudo registrar el huésped correctamente, por favor intentalo nuevamente")
            return redirect('/nuevo_huesped')

    form = NuevoHesped()
    return render(request, 'nuevo_huesped.html', {'form':form})


@login_required(login_url='/login')   
def editar_huesped(request, id):

    instancia = Guest.objects.get(id=id)
    form = EditarHuesped(instance=instancia)

    if request.method == "POST":
     
        form = EditarHuesped(request.POST, instance=instancia)

        if form.is_valid():
    
            instancia = form.save(commit=False)
     
            instancia.save()

            messages.success(request, 'Se editó el huésped correctamente')
            return redirect('/huespedes')

        else:

            messages.error(request, 'No se pudo editar el huésped , por favor intentalo nuevamente')
            return redirect(request, '/editar_huesped')


    return render(request, "editar_huesped.html", {'form': form})


@login_required(login_url='/login')
def eliminar_huesped(request, id):
    if request.user.is_authenticated:
        instancia = Guest.objects.get(id=id)
        instancia.delete()

        messages.success(request, 'Se eliminó el huésped')
        return redirect('/huespedes')
    else:
        return redirect('/login')

#------------------------------------------------- vistas proovedor -------------------------------------------------

def proveedores(request):
    if request.user.is_authenticated:
        proovider_list = Proovider.objects.all()
        user_filter = ProviderFilter(request.GET, queryset=proovider_list)
        return render(request, 'proveedores.html', {'filter': user_filter})
    else:
        return redirect('/login')


@login_required(login_url='/login')
def nuevo_proveedor(request):
    form = NuevoProveedor(request.POST)
    if request.method == "POST":

        if form.is_valid():
            form.save()
            rubro = form.cleaned_data.get('rubro')
            email = form.cleaned_data.get('email')
            telefono = form.cleaned_data.get('telefono')
          
            messages.success(request, "El proveedor se registró correctamente")
            return redirect('/proveedores')
        else:
            messages.error(request, "No de pudo registrar el proveedor correctamente, por favor intentalo nuevamente")
            return redirect('/nuevo_proveedor')

    form = NuevoProveedor()
    return render(request, 'nuevo_proveedor.html', {'form':form})


@login_required(login_url='/login')   
def editar_proveedor(request, id):

    instancia = Proovider.objects.get(id=id)
    form = EditarPorveedor(instance=instancia)

    if request.method == "POST":
     
        form = EditarPorveedor(request.POST, instance=instancia)

        if form.is_valid():
    
            instancia = form.save(commit=False)
     
            instancia.save()

            messages.success(request, 'Se editó el proveedor correctamente')
            return redirect('/proveedores')

        else:

            messages.error(request, 'No se pudo editar el proveedor , por favor intentalo nuevamente')
            return redirect(request, '/editar_huesped')


    return render(request, "editar_proveedor.html", {'form': form})


@login_required(login_url='/login')
def eliminar_proveedor(request, id):
    if request.user.is_authenticated:
        instancia = Proovider.objects.get(id=id)
        instancia.delete()

        messages.success(request, 'Se eliminó el proveedor')
        return redirect('/proveedores')
    else:
        return redirect('/login')

#------------------------------------------------- vistas reservas y facturas -------------------------------------------------

def solicitud_reservas(request):
    if request.user.is_authenticated:
        booking_client_list = Booking_Client.objects.all().order_by('-fecha_creacion')
        user_filter = BookingFilter(request.GET, queryset=booking_client_list)
        return render(request, 'solicitud_reservas.html', {'filter': user_filter})
    else:
        return redirect('/login')


@login_required(login_url='/login')   
def ver_estado(request, id):

    instancia = Booking_Client.objects.get(id=id)
    form = VerReservacion(instance=instancia)

    if request.method == "POST":
     
        form = VerReservacion(request.POST, instance=instancia)

        if form.is_valid():
    
            instancia = form.save(commit=False)
     
            instancia.save()

            messages.success(request, 'Se cambio el estado de la solicitud')
            return redirect('/solicitud_reservas')

        else:

            messages.error(request, 'No se cambio el estado de la reservación')
            return redirect(request, '/ver_estado')


    return render(request, "ver_estado.html", {'form': form})

@login_required(login_url='/login')
def eliminar_solicitud(request, id):
    if request.user.is_authenticated:
        instancia = Booking_Client.objects.get(id=id)
        instancia.delete()

        messages.success(request, 'Se eliminó la solicitud de reserva')
        return redirect('/solicitud_reservas')
    else:
        return redirect('/login')


def facturas(request):
    if request.user.is_authenticated:
        ticket_list = Ticket.objects.all()
        user_filter = TicketFilter(request.GET, queryset=ticket_list)
        return render(request, 'facturas.html', {'filter': user_filter})
    else:
        return redirect('/login')


class Detalle_Factura(LoginRequiredMixin, DetailView):
    model = Ticket
    template_name = 'detalle_factura.html'

    login_url = '/login'


def nueva_factura(request):
    form = CrearFactura(request.POST)
    if request.method == "POST":

        if form.is_valid():
            form.save()

            fecha_boleta = form.cleaned_data.get('fecha_boleta')
            tipo_habitacion = form.cleaned_data.get('tipo_habitacion')
            precio_servivcio = form.cleaned_data.get('precio_servivcio')
            noches = form.cleaned_data.get('noches')
            precio_noches = form.cleaned_data.get('precio_noches')
            personas = form.cleaned_data.get('personas')
            precio_personas = form.cleaned_data.get('precio_personas')
            total = form.cleaned_data.get('total')
            from_user = form.cleaned_data.get('from_user')
            to_user = form.cleaned_data.get('to_user')
         
            messages.success(request, "La factura se creó correctamente")
            return redirect('/facturas')
        else:
            messages.error(request, "No de puso crear la factura correctamente, por favor intentalo nuevamente")
            return redirect('/nueva_factura')

    form = CrearFactura()
    return render(request, 'nueva_factura.html', {'form':form})

@login_required(login_url='/login')
def eliminar_factura(request, id):
    if request.user.is_authenticated:
        instancia = Ticket.objects.get(id=id)
        instancia.delete()

        messages.success(request, 'Se eliminó la factura')
        return redirect('/facturas')
    else:
        return redirect('/login')







  
    
    



