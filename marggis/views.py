from django.shortcuts import render, redirect
from .models import usuario as XD, Genero, Producto
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def index(request):
    context={}
    return render(request, 'paginas/index.html', context)

#PRODUCTO

def productos(request):
    productos = Producto.objects.all()
    data = {
        'productos' : productos
    }
    return render(request, 'paginas/productos.html', data)

#REGISTRO
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        existing_user = User.objects.filter(username=username).exists()
        if existing_user:
            messages.error(request, 'El nombre de usuario ya está registrado.')
            return redirect('registro')

        genero_id = request.POST.get('genero')
        correo = request.POST.get('correo')
        contraseña = request.POST.get('contraseña')

        if User.objects.filter(username=username).exists():
            mensaje = 'El usuario ya está registrado. Por favor, elige otro nombre de usuario.'
            generos = Genero.objects.all()
            context = {'generos': generos, 'mensaje': mensaje}
            return render(request, 'paginas/registro.html', context)

        genero = Genero.objects.get(id_genero=genero_id)
        user = User.objects.create_user(username=username, email=correo, password=contraseña)
        obj = XD.objects.create(usuario=user, id_genero=genero, correo=correo, contraseña=contraseña)

        mensaje = 'Registro exitoso. Ahora puedes iniciar sesión.'
        context = {'mensaje': mensaje}
        return render(request, 'paginas/login.html', context)
    else:
        generos = Genero.objects.all()
        context = {'generos': generos}
        return render(request, 'paginas/registro.html', context)
#LOGIN
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Verificar las credenciales del usuario
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Credenciales válidas, iniciar sesión
            login(request,user)
            return redirect('index')
        else:
            # Credenciales inválidas, mostrar mensaje de error
            messages.error(request, 'Usuario o contraseña incorrectos.')
            return redirect('login')
    
    return render(request, 'paginas/login.html')

