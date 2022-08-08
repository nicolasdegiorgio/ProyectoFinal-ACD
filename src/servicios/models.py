from django.db import models
# Create your models here.


class Detailing (models.Model):
    
    cliente = models.IntegerField() #se va a identificar con el documento
    turno = models.CharField(max_length=30)
    status = models.CharField(max_length=30)