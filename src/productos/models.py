from django.db import models

# Create your models here.
class ProductosDetailing (models.Model):
    nombre = models.CharField(max_length=150)
    marca = models.CharField(max_length=150)
    precio = models.FloatField()
    tipo = models.CharField(max_length=20, default='Detailing') #Todavia no se le da mucha utilidad
    stock = models.IntegerField(default=50)
    
    #Defino el str para ver en el panel de administración
    def __str__(self) -> str:
        return f'Nombre: {self.nombre} - Precio: ${self.precio}'
    

# class ProductosLimpieza(models.Model):
    
#     nombre = models.CharField(max_length=150)
#     marca = models.CharField(max_length=150)
#     precio = models.FloatField()
#     tipo = models.DateField(max_length=10) #Todavia no se le da mucha utilidad
#     stock = models.IntegerField(default=50)
    
#     #Defino el str para ver en el panel de administración
#     def __str__(self) -> str:
#         return f'Nombre: {self.nombre} - Precio: ${self.precio}'