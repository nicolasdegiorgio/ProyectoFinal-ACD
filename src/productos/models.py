from datetime import datetime, timezone

from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class ProductosDetailing (models.Model):
    nombre = models.CharField(max_length=150)
    marca = models.CharField(max_length=150)
    precio = models.FloatField()
    tipo = models.CharField(max_length=20, default='Detailing')
    stock = models.IntegerField(default=50)
    fecha_carga = models.DateTimeField(auto_now_add=True, null=True)
    imagen = models.ImageField(upload_to = 'productos_imagenes', null = True)
    descripcion = RichTextField(null=True)
    
    
    #Defino el str para ver en el panel de administración
    def __str__(self) -> str:
        return f'Nombre: {self.nombre} - Precio: ${self.precio}'
    
    

class Comentarios(models.Model):
    producto = models.ForeignKey(ProductosDetailing, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    contenido = models.TextField()


    def __str__(self):
        return f'Comentario en {self.producto.nombre}  {self.producto.marca} por {self.usuario}'
    
