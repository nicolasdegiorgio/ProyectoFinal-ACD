from datetime import datetime,timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ProductosDetailing (models.Model):
    nombre = models.CharField(max_length=150)
    marca = models.CharField(max_length=150)
    precio = models.FloatField()
    tipo = models.CharField(max_length=20, default='Detailing')
    stock = models.IntegerField(default=50)
    descuento = models.IntegerField(default=0)
    fecha_carga = models.DateTimeField(auto_now_add=True, null=True)
    
    #Defino el str para ver en el panel de administración
    def __str__(self) -> str:
        return f'Nombre: {self.nombre} - Precio: ${self.precio}'
    
    
    def aplicar_descuento (self):
        
        if self.descuento > 0:
            nuevo_precio = self.precio*(1-self.descuento/100)
            self.precio = nuevo_precio
            self.save
            

class Comentarios(models.Model):
    producto = models.ForeignKey(ProductosDetailing, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    contenido = models.TextField()


    def __str__(self):
        return f'Comentario en {self.producto.nombre}  {self.producto.marca} por {self.usuario}'
    
