from django.db import models
from clientes.models import Usuarios
# Create your models here.


class Detailing (models.Model):
    
    cliente = models.IntegerField(max_length=30) #se va a identificar con el documento
    turno = models.DateField()
    status = models.BooleanField()