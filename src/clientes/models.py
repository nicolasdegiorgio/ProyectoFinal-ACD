from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Avatar(models.Model):

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)
    
class Contacto(models.Model):
    MOTIVO_DE_CONTACTO_CHOICES = [
        ('VENDEDOR', 'Quiero ser vendedor'),
        ('COMPRA', 'Quiero comprar')
    ]
    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    motivo_contacto = models.CharField(
        max_length=20,
        choices=MOTIVO_DE_CONTACTO_CHOICES,
        default='VENDEDOR'
    )
    contenido = RichTextField()
    
    def __str__(self):
        return f'{self.usuario} - {self.motivo_contacto} comentó lo siguiente: {self.contenido}'
    
    