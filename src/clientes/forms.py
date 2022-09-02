from dataclasses import fields
from django.forms import Form, CharField, IntegerField, EmailField, DateField, PasswordInput, ImageField, ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from clientes.models import Contacto


class CrearUsuario (Form):
    
    nombre = CharField (max_length=50)
    apellido = CharField (max_length=50)
    documento = IntegerField()
    email = EmailField( max_length=254)
    
class UserCustomCreationForm(UserCreationForm):
    email = EmailField()
    password1 = CharField(label='Contraseña', widget=PasswordInput)
    password2 = CharField(label='Repita la contraseña', widget=PasswordInput)
    first_name = CharField(label='Nombre')
    last_name = CharField(label='Apellido')
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2','first_name','last_name']
        help_text = {'email':'', 'password1':'', 'password2':''}
        
class UserEditForm(UserCreationForm):
    first_name = CharField(label='Nombre')
    last_name = CharField(label='Apellido')
    email = EmailField()
    password1 = CharField(label='Contraseña', widget=PasswordInput)
    password2 = CharField(label='Repita la contraseña', widget=PasswordInput)
    
    class Meta:
        model = User
        fields = ['first_name','last_name', 'email', 'password1', 'password2']
        help_text = {'first_name':'Nombre completo','last_name': 'Apellido', 'email':'ingrese su email principal', 'password1':'', 'password2':''}
        
        
class AvatarForm(Form):
    imagen = ImageField()
    
    
    
class ContactForm(ModelForm):
    class Meta:
        model = Contacto
        fields=['motivo_contacto','contenido']