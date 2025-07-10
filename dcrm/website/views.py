# Importa la función render, que permite combinar una plantilla HTML con datos y devolver una respuesta HTTP.
from django.shortcuts import render, redirect
# Importa el modelo User de Django, que representa a los usuarios en la base de datos.

from .models import Record

# Importa funciones para autenticación de usuarios:
# - authenticate: verifica credenciales.
# - login: inicia sesión.
# - logout: cierra sesión.
from django.contrib.auth import authenticate, login, logout


# Importa el sistema de mensajes de Django para mostrar notificaciones al usuario.
from django.contrib import messages

from .forms import SignUpForm, AddRecordForm

from django.core.paginator import Paginator


def register_user(request):
    return render(request, 'register.html', {})

# Aquí se deben crear las vistas de la aplicación.
# Esta función define la vista principal (home) del sitio.
# region Home
def home(request):
    records = Record.objects.all().order_by('-created_at')  # Todos los registros ordenados

    # ✅ CORREGIDO: usamos "records", no "records_list"
    paginator = Paginator(records, 10)  # 10 registros por página 
    page_number = request.GET.get('page')  # Obtiene el número de página de la solicitud GET
    records = paginator.get_page(page_number)  # Obtiene la página actual de registros

    if request.method == 'POST':
        username = request.POST['username']
        if not username:
            messages.error(request, "⛔ El nombre de usuario es obligatorio!")
            return redirect('home')

        password = request.POST['password']
        if not password:
            messages.error(request, "⛔ La contraseña es obligatoria!")
            return redirect('home')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "🙌 Has iniciado sesión!")
            return redirect('home')
        else:
            messages.error(request, "⛔ Credenciales inválidas!")
            return redirect('home')

    return render(request, 'home.html', {'records': records}) #
# Renderiza la plantilla 'home.html' y pasa los registros como contexto.
# Esta función define la vista de creación de registros (add_record) del sitio.
# Esta función define la vista de inicio de sesión (login) del sitio.
# endregion


# Esta función define la vista de inicio de sesión (login) del sitio.


def login_user(request):
    pass
def logout_user(request):
    logout(request)# Cierra la sesión del usuario.
    # Muestra un mensaje de éxito al usuario.
    messages.success(request, "You Have Been Logged Out!")# Muestra un mensaje de éxito al usuario. 
    return redirect('home')# Redirige al usuario a la página de inicio (home).
# Esta función define la vista de cierre de sesión (logout) del sitio.

def register_user(request):
    # Si la solicitud es POST, significa que el usuario envió el formulario
    if request.method == 'POST':
        form = SignUpForm(request.POST)  # Llenamos el formulario con los datos recibidos
        if form.is_valid():  # Validamos que los datos cumplan con las reglas
            form.save()  # Guardamos el nuevo usuario en la base de datos


            # Autenticamos al usuario con sus credenciales recién registradas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)  # Iniciamos sesión automáticamente


            messages.success(request, "¡Registro exitoso! Bienvenido.")  # Mensaje de bienvenida
            return redirect('home')  # Redirigimos al usuario a la página principal


    else:
        form = SignUpForm()  # Si es GET, mostramos el formulario vacío


    # Renderizamos el formulario (en caso de GET o si el formulario no es válido)
    return render(request, 'register.html', {'form': form})

def customer_record(request, pk):# Esta función define la vista de un registro específico (customer_record) del sitio.
    if request.user.is_authenticated:# Verifica si el usuario está autenticado.
        # Intenta obtener el registro del cliente con el ID proporcionado (pk).
        # Si no se encuentra, se lanzará una excepción Record.DoesNotExist.
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record':customer_record})# Renderiza la plantilla 'record.html' y pasa el registro del cliente como contexto.
    # Si el usuario no está autenticado, redirige a la página de inicio con un mensaje de error.
    else:# Si el usuario no está autenticado.
        # Muestra un mensaje de error al usuario.
        messages.success(request, "You Must Be Logged In To View That Page...")# Muestra un mensaje de error al usuario.
        # Redirige al usuario a la página de inicio (home).
        return redirect('home')

def delete_record(request, pk): # Esta función define la vista para eliminar un registro específico (delete_record) del sitio.
    # Verifica si el usuario está autenticado.
    if request.user.is_authenticated: # Verifica si el usuario está autenticado.
        delete_it = Record.objects.get(id=pk)# Obtiene el registro del cliente con el ID proporcionado (pk).
        # Si el registro existe, lo elimina.
        delete_it.delete()# Elimina el registro del cliente.
        # Muestra un mensaje de éxito al usuario.
        messages.success(request, "Record Deleted Successfully...")# Muestra un mensaje de éxito al usuario.
        # Redirige al usuario a la página de inicio (home).
        return redirect('home')# Redirige al usuario a la página de inicio (home).
    # Si el usuario no está autenticado, muestra un mensaje de error y redirige a la página de inicio.
    else:# Si el usuario no está autenticado.
        messages.success(request, "You Must Be Logged In To Do That...")# Muestra un mensaje de error al usuario.
        # Redirige al usuario a la página de inicio (home).
        return redirect('home')# Redirige al usuario a la página de inicio (home).
# Esta función define la vista para agregar un nuevo registro (add_record) del sitio.

def add_record(request):# Esta función define la vista para agregar un nuevo registro (add_record) del sitio.
# Verifica si el usuario está autenticado.
    form = AddRecordForm(request.POST or None)# Crea una instancia del formulario AddRecordForm, pasando los datos POST si están disponibles, o None si no hay datos POST.
    if request.user.is_authenticated:# Verifica si el usuario está autenticado.
        # Si el método de la solicitud es POST, significa que se está enviando un formulario.
        if request.method == "POST": # Verifica si la solicitud es POST.
            if form.is_valid():# Verifica si el formulario es válido.
                # Si el formulario es válido, guarda el nuevo registro en la base de datos.
                add_record = form.save()# Guarda el nuevo registro en la base de datos.
                messages.success(request, "Record Added...")# Muestra un mensaje de éxito al usuario.
                # Redirige al usuario a la página de inicio (home).
                return redirect('home')# Redirige al usuario a la página de inicio (home).
        # Si el método de la solicitud no es POST, simplemente renderiza la plantilla 'add_record.html'.
        return render(request, 'add_record.html', {'form':form})# Renderiza la plantilla 'add_record.html' y pasa el formulario como contexto.
    # Si el usuario no está autenticado, muestra un mensaje de error y redirige a la página de inicio.
    else:# Si el usuario no está autenticado.
        # Muestra un mensaje de error al usuario.
        messages.success(request, "You Must Be Logged In...")# Muestra un mensaje de error al usuario.
        # Redirige al usuario a la página de inicio (home).
        return redirect('home')# Redirige al usuario a la página de inicio (home).

def update_record(request, pk):# Esta función define la vista para actualizar un registro específico (update_record) del sitio.
# Verifica si el usuario está autenticado.
    if request.user.is_authenticated:# Verifica si el usuario está autenticado.
        # Obtiene el registro del cliente con el ID proporcionado (pk).
        current_record = Record.objects.get(id=pk)# Obtiene el registro del cliente con el ID proporcionado (pk).
        # Crea una instancia del formulario AddRecordForm, pasando los datos POST si están disponibles y el registro actual como instancia.
        form = AddRecordForm(request.POST or None, instance=current_record)# Crea una instancia del formulario AddRecordForm, pasando los datos POST si están disponibles y el registro actual como instancia.
        # Si el método de la solicitud es POST, significa que se está enviando el formulario.
        if form.is_valid():# Verifica si el formulario es válido.
            # Si el formulario es válido, guarda los cambios en el registro.
            form.save()# Guarda los cambios en el registro.
            messages.success(request, "Record Has Been Updated!")#3 Muestra un mensaje de éxito al usuario.
            # Redirige al usuario a la página de inicio (home).
            return redirect('home')# Redirige al usuario a la página de inicio (home).
        return render(request, 'update_record.html', {'form':form})# Renderiza la plantilla 'update_record.html' y pasa el formulario como contexto.
    else:# Si el usuario no está autenticado.
        # Muestra un mensaje de error al usuario.
        messages.success(request, "You Must Be Logged In...")# Muestra un mensaje de error al usuario.
        # Redirige al usuario a la página de inicio (home).
        return redirect('home')# Redirige al usuario a la página de inicio (home).
# Renderiza la plantilla 'update_record.html' y pasa el formulario como contexto.

