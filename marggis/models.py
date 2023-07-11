from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Genero(models.Model):
    id_genero  = models.AutoField(db_column='idGenero', primary_key=True) 
    genero     = models.CharField(max_length=20, blank=False, null=False)
    def __str__(self):
        return str(self.genero)
    
class usuario(models.Model):
    id_usuario = models.AutoField(db_column='idUsuario',primary_key=True) 
    usuario = models.CharField(max_length=50, unique=True)
    id_genero  = models.ForeignKey('Genero',on_delete=models.CASCADE, db_column='idGenero') 
    correo = models.EmailField(max_length=200, unique=True)
    contraseña = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return str(self.usuario)


class Producto(models.Model):
    id_nombre = models.AutoField(db_column='idNombre',primary_key=True) 
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="productos", null=True)
    def __str__(self):
        return self.nombre
    
opciones_consultas = [
    [0, "Consulta"],
    [1,"Reclamo"],
    [2,"Sugerencia"],
    [3,"Felicitaciones"]
]

class Contacto(models.Model):
    nombre= models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices= opciones_consultas)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def __str__(self):
        return self.nombre   