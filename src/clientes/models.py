from django.db import models

# Create your models here.
class Usuarios (models.Model):
    
    nombre = models.CharField (max_length=50)
    apellido = models.CharField (max_length=50)
    documento = models.IntegerField()
    email = models.EmailField( max_length=254)
    