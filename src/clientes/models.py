from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Usuarios (models.Model):
    
    nombre = models.CharField (max_length=50)
    apellido = models.CharField (max_length=50)
    documento = models.IntegerField()
    email = models.EmailField( max_length=254)
    
    
class Avatar(models.Model):

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)

    