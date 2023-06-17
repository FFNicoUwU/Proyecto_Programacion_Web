from django.shortcuts import render
from .models import Alumno, Genero
from .forms import GeneroForm
from django.shortcuts import redirect

def index(request):
    alumnos = Alumno.objects.all()
    context = {"alumnos": alumnos}
    return render(request, 'index.html', context)

def crud(request):
    alumnos = Alumno.objects.all()
    context = {"alumnos": alumnos}
    return render(request, 'alumnos_list.html', context)

def alumnosAdd(request):
    if request.method != "POST":
        # no es un POST por lo tanto se muestra el formulario para agregar
        generos = Genero.objects.all()
        context = {"generos": generos}
        return render(request, 'alumnos_add.html', context)
    else:
        print("--->>>> llego al else de addAlumnos crea el objeto ")
        # Es un POST, por lo tanto se recuperan los datos del formulario
        # y se graban en la tabla
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        aPaterno = request.POST["paterno"]
        aMaterno = request.POST["materno"]
        fechaNac = request.POST["fechaNac"]
        genero = request.POST["genero"]
        telefono = request.POST["telefono"]
        email = request.POST["email"]
        direccion = request.POST["direccion"]
        activo = "1"  # ---> esta linea no será tomada en cuenta en la creación dado que se asigna 1 arbitrariamente

        objGenero = Genero.objects.get(id_genero=genero)
        obj = Alumno.objects.create(rut=rut,
                                    nombre=nombre,
                                    apellido_paterno=aPaterno,
                                    apellido_materno=aMaterno,
                                    fecha_nacimiento=fechaNac,
                                    id_genero=objGenero,
                                    telefono=telefono,
                                    email=email,
                                    direccion=direccion,
                                    activo=1)
        obj.save()
        context = {"mensaje": "OK, datos grabados..."}
        return render(request, 'alumnos_add.html', context)


def alumnos_del(request, pk):
    context = {}
    try:
        alumno = Alumno.objects.get(rut=pk)
        print("REGISTRO A ELIMINAR============>>>")
        print(alumno)
        alumno.delete()
        print("ELIMINADOR============>>>")
        mensaje = "Bien, dato eliminado!!!"
        alumnos = Alumno.objects.all()
        context = {"alumnos": alumnos, "mensaje": mensaje}
        return render(request, "alumnos_list.html", context)
    except:
        mensaje = "Error, el rut  no existe!!!"
        alumnos = Alumno.objects.all()
        context = {"alumnos": alumnos, "mensaje": mensaje}
        return render(request, "alumnos_list.html", context)


def alumnos_findEdit(request, pk):
    if pk != "":
        alumno = Alumno.objects.get(rut=pk)
        print(alumno)
        generos = Genero.objects.all()
        print("generos--->>>")
        print(generos)

        print(type(alumno.id_genero.genero))
        context = {"alumno": alumno, "generos": generos}
        if alumno:
            return render(request, "alumnos_edit.html", context)
        else:
            context = {"mensaje": "Error, rut no existe"}
            return render(request, "alumnos_list.html", context)


def alumnosUpdate(request):
    if request.method == "POST":
        # Es un POST, por lo tanto se recuperan los datos del formulario
        # y se graban en la tabla
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        aPaterno = request.POST["paterno"]
        aMaterno = request.POST["materno"]
        fechaNac = request.POST["fechaNac"]
        print("=========>>>")
        print(fechaNac)
        print("<<<<=========")
        genero = request.POST["genero"]
        telefono = request.POST["telefono"]
        email = request.POST["email"]
        direccion = request.POST["direccion"]
        activo = "1"

        objGenero = Genero.objects.get(id_genero=genero)
        alumno = Alumno()
        alumno.rut = rut
        alumno.nombre = nombre
        alumno.apellido_paterno = aPaterno
        alumno.apellido_materno = aMaterno
        alumno.fecha_nacimiento = fechaNac
        alumno.id_genero = objGenero
        alumno.telefono = telefono
        alumno.email = email
        alumno.direccion = direccion
        alumno.activo = 1
        alumno.save()

        generos = Genero.objects.all()
        context = {"mensaje": "OK, datos actualizados...",
                   "generos": generos, "alumno": alumno}
        return render(request, 'alumnos_edit.html', context)
    else:
        # NO es por POST, por lo tanto solo se muestra el formulario para agregar
        alumnos = Alumno.objects.all()
        context = {"alumnos": alumnos}
        return render(request, 'alumnos_list.html', context)

def listadoSQL(request):
    alumnos = Alumno.objects.raw('SELECT * FROM alumnos_alumno')
    print(alumnos)
    context = {"alumnos": alumnos}
    return render(request, 'listadoSQL.html', context)


def generosAdd(request):
    if request.method == "POST":
        form = GeneroForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            form = GeneroForm()
            return render(request, "agregar_genero.html",{'form': form})
    else:
        form = GeneroForm()
        return render(request, "agregar_genero.html",{'form': form})














