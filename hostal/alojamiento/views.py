from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
import time
from .models import *
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from .forms import SignUpForm,PasswordChangingForm, EditarUsuario, EditarPermiso, CrearHabitacion, EditarHabitacion, EditarPerfil, EditarTrabajador,EditarInfo,VerReservacion, CrearFactura, EditarFactura, NuevoHesped, EditarHuesped, NuevoProveedor, EditarPorveedor, CrearPlato, EditarPlato, NuevoEmpleado, NuevoPedido, EditarPedido, NuevoProducto, EditarProducto, AgregarStock, OcuparStock, EstadoOrden, EditarPost
from django.contrib.auth.views import PasswordChangeView
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .filters import UserFilter, RoomFilter, GuestFilter, BookingFilter, TicketFilter, ProviderFilter, DishesFilter, EmployeeFilter, OrderProoviderFilter, ProductFilter, RoomUserFilter
from django.contrib.auth.decorators import login_required


# Create your views here.

#-------------------------- vistas opiniones, reserva_cliente e index -------------------------
class Homeview(ListView):
    model = Post
    template_name = 'index.html'


def ayuda(request):
    if request.user.is_authenticated:
        return render(request, 'ayuda.html')
    else:
        return redirect('/login') 

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False

    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True 

    return HttpResponseRedirect(reverse('opiniones', args=[str(pk)]))


class Opiniones(DetailView):
    model = Post
    template_name = 'opiniones.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Opiniones, self).get_context_data(*args, **kwargs)

        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True    


        context["total_likes"] = total_likes 
        context["liked"] = liked
        return context

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



#------------------ crud de publicaciones ----------------------

def nuevo_post(request):
    if request.user.is_authenticated:
        return render(request, 'posts.html')
    else:
        return redirect('/login')   

def crear_post(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            mi_user = request.POST['user_id']
            mi_titulo = request.POST['Titulo']
            mi_imagen = request.FILES['imagen']
            
            if mi_titulo != "" :
                try:
                    
                    post = Post()

                    post.user_id  = mi_user 
                    post.Titulo = mi_titulo
                    post.imagen = mi_imagen
                    post.activo = 1

                    post.save()
                
                    return redirect('/')
                    
                except post.DoesNotExist:
                    messages.error(request, 'Tú comentario no se pudo publicar, por favor intententalo nuevamente')
                    return redirect('/nuevo_post')
            
            else:
                messages.error(request, 'lo sentimos, tú comentario no se pudo publicar, por favor intententalo nuevamente ')
                return redirect('/nuevo_post')
        
        else:
            messages.error(request, 'El metodo post es incorrecto ')
            return redirect('/nuevo_post')
    
    else: 
        return redirect('/login')  

@login_required(login_url='/login')   
def editar_post(request, id):

    instancia = Post.objects.get(id=id)
    form = EditarPost(instance=instancia)

    if request.method == "POST":
     
        form = EditarPost(request.POST, instance=instancia)

        if form.is_valid():
    
            instancia = form.save(commit=False)
     
            instancia.save()

            messages.success(request, 'Se editó la publicación correctamente')
            return redirect('/dashboard')

        else:

            messages.error(request, 'No se pudo editar la publicación, por favor intentalo nuevamente')
            return redirect(request, '/editar_post')


    return render(request, "editar_post.html", {'form': form})

def eliminar_post(request, id):
    instancia = Post.objects.get(id=id)
    instancia.delete()

    messages.success(request, 'Se eliminó a tú publicación ')
    return redirect('/dashboard')

#------------------ comentarios y respuestas  ----------------------

def publicar_comentario(request, pk):
    if request.user.is_authenticated:
        if request.method == "POST":
            mi_post = request.POST['post_id']
            mi_user = request.POST['user_id']
            mi_texto = request.POST['texto']
            
            if mi_texto != "":
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


def publicar_respuesta(request, pk):
    if request.user.is_authenticated:
        if request.method == "POST":
            mi_comment = request.POST['comment_id']
            mi_user = request.POST['user_id']
            mi_texto = request.POST['texto']
            
            if mi_texto != "" :
                try:
                    
                    answer = Answer()

                    answer.comment_id  = mi_comment 
                    answer.user_id  = mi_user 
                    answer.texto = mi_texto
                    answer.activo = 1

                    answer.save()
                    
                    return HttpResponseRedirect(reverse('opiniones', args=[str(pk)]))

                except answer.DoesNotExist:
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


#--------------------------- vistas rooms clientes ------------------------------#

def all_rooms(request):
    if request.user.is_authenticated:
        room_list = Room.objects.all()
        user_filter = RoomUserFilter(request.GET, queryset=room_list)
        return render(request, 'all_rooms.html', {'filter': user_filter})
    else:
        return redirect('/login')

class Rooms(LoginRequiredMixin, DetailView):
    model = Room
    template_name = 'detalle_habitacion.html'

    login_url = '/login'

class Reservar(LoginRequiredMixin, DetailView):
    model = Room
    template_name = 'reservar.html'

    login_url = '/login'

def nueva_reservacion(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            mi_user = request.POST['user_id']
            mi_numero_h     = request.POST['numero_habitacion']
            mi_tipo_h       = request.POST['tipo_habitacion']
            mi_tipo_c       = request.POST['tipo_cama']
            mi_cantidad_c   = request.POST['cantidad_camas']
            mi_precio       = request.POST['precio']
            mi_nombre       = request.POST['nombre']
            mi_apellido     = request.POST['apellido']
            mi_rut          = request.POST['rut']
            mi_nombre2      = request.POST['nombre2']
            mi_apellido2    = request.POST['apellido2']
            mi_rut2         = request.POST['rut2']
            mi_f_llegada    = request.POST['fecha_llegada']
            mi_f_salida     = request.POST['fecha_salida']
            mi_mensaje      = request.POST['mensaje']

            
            if mi_user != "" or mi_numero_h != "" or mi_tipo_h != "" or mi_tipo_c != "" or mi_cantidad_c != "" or mi_precio != "" or mi_nombre != ""  or mi_apellido !="" or mi_rut != "":
                try:
                    
                    booking_client = Booking_Client()

                    booking_client.user_id  = mi_user 
                    booking_client.numero_habitacion = mi_numero_h
                    booking_client.tipo_habitacion = mi_tipo_h
                    booking_client.tipo_cama = mi_tipo_c
                    booking_client.cantidad_camas = mi_cantidad_c
                    booking_client.precio = mi_precio
                    booking_client.nombre = mi_nombre
                    booking_client.apellido = mi_apellido
                    booking_client.rut = mi_rut
                    booking_client.nombre2 = mi_nombre2
                    booking_client.apellido2 = mi_apellido2
                    booking_client.rut2 = mi_rut2
                    booking_client.fecha_llegada = mi_f_llegada
                    booking_client.fecha_salida = mi_f_salida
                    booking_client.mensaje = mi_mensaje
                    booking_client.activo = 1

                    booking_client.save()
                
                    messages.success(request, 'Tú reservación se envió exitosamente')
                    return redirect('/mis_reservas')

                    
                except booking_client.DoesNotExist:
                    messages.error(request, 'Tú reservación no se pudo enviar,  por favor intententalo nuevamente')
                    return redirect('/all_rooms')
            
            else:
                messages.error(request, 'lo sentimos, Tú reservación no se pudo enviar, por favor intententalo nuevamente ')
                return redirect('/all_rooms')
        
        else:
            messages.error(request, 'El metodo post es incorrecto ')
            return redirect('/all_rooms')
    
    else: 
        return redirect('/login')   


#--------------------------- vistas reservas ------------------------------#


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


#------------------------------------------------ dashboard proveedor -------------------------------------------------

def login_proveedores(request):
    form = AuthenticationForm()
    if request.method == "POST":

        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                do_login(request, user)

            return redirect('/index_proveedor')
        else:
            messages.error(request, "Verifique Bien su Usuario y Contraseña")
            return redirect('/login_proveedores')
            
    return render(request, "login_proveedores.html", {'form': form})


def index_proveedor(request, username=None):
    if request.user.is_authenticated:
        
        current_user = request.user
        if username and username != current_user.username:
            user = User.objects.get(username=username)
            orders = user.orders.all()
        else:
            orders = current_user.orders.all().order_by('-fecha_creacion')
            user = current_user

        return render(request, 'index_proveedor.html', {'user':user, 'orders':orders})

    else: 
        return redirect('/login_proveedores')


class EstadoOrdenView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Order
    template_name = 'info_orden.html'
    form_class = EstadoOrden

    success_message = "Estado de el pedido se cambio correctamente"
    success_url = reverse_lazy('index_proveedor')
    login_url = '/login_proveedores'


#------------------------------------------------ vistas perfil -------------------------------------------------

def perfil(request, username=None):
    if request.user.is_authenticated:

        current_user = request.user
        if username and username != current_user.username:
            user = User.objects.get(username=username)
        else:
            user = current_user

        return render(request, 'perfil.html', {'user':user})

    else:
        return redirect('/login')


class EditarPerfilView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = 'editar_perfil.html'
    form_class = EditarPerfil

    success_message = "Tú perfil se editó correctamente"
    success_url = reverse_lazy('perfil')
    login_url = '/login'



class ConfigView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'configuracion.html'
    form_class = EditarInfo

    success_message = "Tú configuración se editó correctamente"
    success_url =  reverse_lazy('perfil')
    login_url = '/login'


class PasswordsChangeView(SuccessMessageMixin, LoginRequiredMixin, PasswordChangeView):
    form_class = PasswordChangingForm
    #form_class = PasswordChangeForm

    success_message = "Tú contraseña se cambio correctamente"
    success_url = reverse_lazy('perfil')
    login_url = '/login'


#----------------------------------- vistas empleados/cargos  -----------------------------------

def empleados(request):
    if request.user.is_authenticated:
        employee_list = Employee.objects.all()
        user_filter = EmployeeFilter(request.GET, queryset=employee_list)
        return render(request, 'empleados.html', {'filter': user_filter})
    else:
        return redirect('/login')

    
@login_required(login_url='/login')
def nuevo_empleado(request):
    form = NuevoEmpleado(request.POST)
    if request.method == "POST":

        if form.is_valid():
            form.save()
            nombre = form.cleaned_data.get('nombre')
            apellido = form.cleaned_data.get('apellido')
            rut = form.cleaned_data.get('rut')
            cargo = form.cleaned_data.get('cargo')
    
            
            messages.success(request, "El empleado se registró correctamente")
            return redirect('/empleados')
        else:
            messages.error(request, "No de pudo registrar el empleado correctamente, por favor intentalo nuevamente")
            return redirect('/nuevo_empleado')

    form = NuevoEmpleado()
    return render(request, 'nuevo_empleado.html', {'form':form})


class EditarEmpleadoView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Employee
    template_name = 'editar_empleado.html'
    form_class = EditarTrabajador

    success_message = "Se editó a tú trabajador correctamente"
    success_url = reverse_lazy('empleados')
    login_url = '/login'


def eliminar_empleado(request, id):
    instancia = Employee.objects.get(id=id)
    instancia.delete()

    messages.success(request, 'Se eliminó a tú trabajador')
    return redirect('/empleados')


#------------------------------------------ vistas administración / Dashboard--------------------------------

def dashboard(request):
    if request.user.is_authenticated:
        users = User.objects.all()
        profiles = Profile.objects.all()
        rooms = Room.objects.all()
        dishes = Dishes.objects.all()
        guests = Guest.objects.all()
        prooviders = Proovider.objects.all()
        tickets = Ticket.objects.all()
        booking_clients = Booking_Client.objects.all()
        employees = Employee.objects.all()
        orders = Order.objects.all()
        products = Product.objects.all()
        posts   = Post.objects.all()
        comments = Comment.objects.all()
        answers = Answer.objects.all()
        context = {'users':users, 'profiles':profiles ,'rooms':rooms, 'dishes':dishes, 'guests':guests, 'prooviders':prooviders, 'tickets':tickets, 'booking_clients':booking_clients,'employees':employees,'orders':orders,'products':products, 'posts':posts,'comments':comments, 'answers':answers}
        return render(request, 'dashboard.html', context)
    else:
        return redirect('/login')


#------------------------------------------------ vistas ususarios --------------------------------

def usuarios(request):
    if request.user.is_authenticated:
        user_list = User.objects.all()
        user_filter = UserFilter(request.GET, queryset=user_list)
        return render(request, 'usuarios.html', {'filter': user_filter})
    else:
        return redirect('/login')


@login_required(login_url='/login')   
def editar_usuario(request, id):

    instancia = User.objects.get(id=id)
    form = EditarUsuario(instance=instancia)

    if request.method == "POST":
     
        form = EditarUsuario(request.POST, instance=instancia)

        if form.is_valid():
    
            instancia = form.save(commit=False)
     
            instancia.save()

            messages.success(request, 'Se editó el usuario')
            return redirect('/usuarios')

        else:

            messages.error(request, 'No se pudo editar el usuario, por favor intentalo nuevamente')
            return redirect(request, '/editar_usuario')


    return render(request, "editar_usuario.html", {'form': form})



@login_required(login_url='/login')   
def editar_permiso(request, id):

    instancia = Profile.objects.get(id=id)
    form = EditarPermiso(instance=instancia)

    if request.method == "POST":
     
        form = EditarPermiso(request.POST, instance=instancia)

        if form.is_valid():
    
            instancia = form.save(commit=False)
     
            instancia.save()

            messages.success(request, 'Se editó el permiso del usuario correctamente')
            return redirect('/usuarios')

        else:

            messages.error(request, 'No se pudo editar el permiso del usuario, por favor intentalo nuevamente')
            return redirect(request, '/editar_permiso')


    return render(request, "editar_permiso.html", {'form': form})


@login_required(login_url='/login')
def eliminar_usuario(request, id):
    if request.user.is_authenticated:
        instancia = User.objects.get(id=id)
        instancia.delete()

        messages.success(request, 'Se eliminó el usuario')
        return redirect('/usuarios')
    else:
        return redirect('/login')


#------------------------------------------------ vistas habitaciones --------------------------------

def habitaciones(request):
    if request.user.is_authenticated:
        room_list = Room.objects.all().order_by('-numero_habitacion')
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

class EditarHabitacionView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Room
    template_name = 'editar_habitacion.html'
    form_class = EditarHabitacion

    success_message = "Se Editó la Habitación"
    success_url = reverse_lazy('habitaciones')
    login_url = '/login'

   
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
      
            messages.success(request, "El plato se creó correctamente")
            return redirect('/comedor')
        else:
            messages.error(request, "No de pudo crear El plato correctamente, por favor intentalo nuevamente")
            return redirect('/nuevo_plato')

    form = CrearPlato()
    return render(request, 'nuevo_plato.html', {'form':form})

class EditarPlatoView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Dishes
    template_name = 'editar_plato.html'
    form_class = EditarPlato

    success_message = "Se Editó el plato"
    success_url = reverse_lazy('/comedor')
    login_url = '/login'



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

class EditarHuespedView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Guest
    template_name = 'editar_huesped.html'
    form_class = EditarHuesped

    success_message = "Se editó el huésped correctamente"
    success_url = reverse_lazy('huespedes')
    login_url = '/login'


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



class EditarProveedorView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Proovider
    template_name = 'editar_proveedor.html'
    form_class = EditarPorveedor

    success_message = "Se editó el proveedor correctamente"
    success_url = reverse_lazy('proveedores')
    login_url = '/login'



@login_required(login_url='/login')
def eliminar_proveedor(request, id):
    if request.user.is_authenticated:
        instancia = Proovider.objects.get(id=id)
        instancia.delete()

        messages.success(request, 'Se eliminó el proveedor')
        return redirect('/proveedores')
    else:
        return redirect('/login')

#------------------------------------------------- vistas reservas u orden de compra ----------------------------------------

def orden_compras(request):
    if request.user.is_authenticated:
        booking_client_list = Booking_Client.objects.all().order_by('-fecha_creacion')
        user_filter = BookingFilter(request.GET, queryset=booking_client_list)
        return render(request, 'orden_compras.html', {'filter': user_filter})
    else:
        return redirect('/login')

class Detalle_Reserva(LoginRequiredMixin, DetailView):
    
    model = Booking_Client
    template_name = 'detalle_reserva.html'

    login_url = '/login'


class EstadoReservaView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Booking_Client
    template_name = 'estado_reserva.html'
    form_class = VerReservacion

    success_message = "Se cambio el estado de la orden de compra"
    success_url = reverse_lazy('orden_compras')
    login_url = '/login'


@login_required(login_url='/login')
def eliminar_solicitud(request, id):
    if request.user.is_authenticated:
        instancia = Booking_Client.objects.get(id=id)
        instancia.delete()

        messages.success(request, 'Se eliminó la solicitud de reserva')
        return redirect('/solicitud_reservas')
    else:
        return redirect('/login')


#----------------------------------------facturas -------------------------------------------------

def facturas(request):
    if request.user.is_authenticated:
        ticket_list = Ticket.objects.all().order_by('-fecha_boleta')
        user_filter = TicketFilter(request.GET, queryset=ticket_list)
        return render(request, 'facturas.html', {'filter': user_filter})
    else:
        return redirect('/login')


class Detalle_Factura(LoginRequiredMixin, DetailView):
    model = Ticket
    template_name = 'detalle_factura.html'

    login_url = '/login'


@login_required(login_url='/login')   
def nueva_factura(request):
    form = CrearFactura(request.POST)
    if request.method == "POST":

        if form.is_valid():
            form.save()
    
            messages.success(request, "La factura se creó correctamente")
            return redirect('/facturas')
        else:
            messages.error(request, "No de pudo crear la factura correctamente, por favor intentalo nuevamente")
            return redirect('/nueva_factura')

    form = CrearFactura()
    return render(request, 'nueva_factura.html', {'form':form})


@login_required(login_url='/login')   
def editar_factura(request, id):

    instancia = Ticket.objects.get(id=id)
    form = EditarFactura(instance=instancia)

    if request.method == "POST":
     
        form = EditarFactura(request.POST, instance=instancia)

        if form.is_valid():
    
            instancia = form.save(commit=False)
     
            instancia.save()

            messages.success(request, 'Se cambio el estado de pago de la factura')
            return redirect('/facturas')

        else:

            messages.error(request, 'No se pudo anular la factura, por favor intentalo nuevamente')
            return redirect(request, '/editar_factura')


    return render(request, "editar_factura.html", {'form': form})


@login_required(login_url='/login')
def eliminar_factura(request, id):
    if request.user.is_authenticated:
        instancia = Ticket.objects.get(id=id)
        instancia.delete()

        messages.success(request, 'Se eliminó la factura')
        return redirect('/facturas')
    else:
        return redirect('/login')


#------------------------------------------------- vistas Ordenes_proveedores------------------------------------------------

def orden_pedido(request):
    if request.user.is_authenticated:
        Order_list = Order.objects.all().order_by('-fecha_creacion')
        user_filter = OrderProoviderFilter(request.GET, queryset=Order_list)
        return render(request, 'orden_pedido.html', {'filter': user_filter})

    else:
        return redirect('/login')


@login_required(login_url='/login')
def nuevo_pedido(request):
    form = NuevoPedido(request.POST)
    if request.method == "POST":

        if form.is_valid():
            form.save()
            proveedor = form.cleaned_data.get('proveedor')
            cantidad = form.cleaned_data.get('cantidad')
            mensaje = form.cleaned_data.get('mensaje')
          
            messages.success(request, "La orden se solicitó correctamente")
            return redirect('/orden_pedido')
        else:
            messages.error(request, "No de pudo registrar la orden al proveedor correctamente, por favor intentalo nuevamente")
            return redirect('/nuevo_pedido')

    form = NuevoPedido()
    return render(request, 'nuevo_pedido.html', {'form':form})


class EditarPedidoView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Order
    template_name = 'editar_pedido.html'
    form_class = EditarPedido

    success_message = "Se editó la orden correctamente"
    success_url = reverse_lazy('orden_pedido')
    login_url = '/login'


@login_required(login_url='/login')
def eliminar_pedido(request, id):
    if request.user.is_authenticated:
        instancia = Order.objects.get(id=id)
        instancia.delete()

        messages.success(request, 'Se eliminó el pedido')
        return redirect('/orden_pedido')
    else:
        return redirect('/login')


class Estado_Pedido(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'estado_pedido.html'

    login_url = '/login'


#------------------------------------------------- vistas recepcion de productos ------------------------------------------------

def recepcion_productos(request):
    if request.user.is_authenticated:
        Product_list = Product.objects.all()
        user_filter = ProductFilter(request.GET, queryset=Product_list)
        return render(request, 'recepcion_productos.html', {'filter': user_filter})

    else:
        return redirect('/login')


@login_required(login_url='/login')
def nuevo_producto(request):
    form = NuevoProducto(request.POST)
    if request.method == "POST":

        if form.is_valid():
            form.save()
          
            messages.success(request, "El producto se registró correctamente")
            return redirect('/recepcion_productos')
        else:
            messages.error(request, "No de pudo registrar el producto correctamente, por favor intentalo nuevamente")
            return redirect('/nuevo_producto')

    form = NuevoProducto()
    return render(request, 'nuevo_producto.html', {'form':form})


class EditarProductoView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Product
    template_name = 'editar_producto.html'
    form_class = EditarProducto

    success_message = "Se editó el producto correctamente"
    success_url = reverse_lazy('recepcion_productos')
    login_url = '/login'


@login_required(login_url='/login')
def eliminar_producto(request, id):
    if request.user.is_authenticated:
        instancia = Product.objects.get(id=id)
        instancia.delete()

        messages.success(request, 'Se eliminó el producto')
        return redirect('/recepcion_productos')
    else:
        return redirect('/login')


#------------- agregar y ocupar stock de productos en recepción--------------

class AgregarStockView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Product
    template_name = 'agregar_stock.html'
    form_class = AgregarStock

    success_message = "Se agregó stock al producto correctamente"
    success_url = reverse_lazy('recepcion_productos')
    login_url = '/login'


class OcuparStockView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Product
    template_name = 'ocupar_stock.html'
    form_class = OcuparStock

    success_message = "Se quitó stock al producto correctamente"
    success_url = reverse_lazy('recepcion_productos')
    login_url = '/login'







  
    
    



