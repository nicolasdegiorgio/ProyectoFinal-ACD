from dataclasses import fields
from django.forms import Form, CharField, IntegerField, EmailField, DateField, PasswordInput, ImageField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CrearUsuario (Form):
    
    nombre = CharField (max_length=50)
    apellido = CharField (max_length=50)
    documento = IntegerField()
    email = EmailField( max_length=254)
    
class UserCustomCreation(UserCreationForm):
    first_name = CharField(label='Nombre')
    last_name = CharField(label='Apellido')
    email = EmailField()
    password1 = CharField(label='Contraseña', widget=PasswordInput)
    password2 = CharField(label='Repita la contraseña', widget=PasswordInput)
    
    class Meta:
        model = User
        fields = ['first_name','last_name', 'email', 'password1', 'password2']
        help_text = {'first_name':'Nombre completo','last_name': 'Apellido', 'email':'ingrese su email principal', 'password1':'', 'password2':''}
        
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
        
        
class Avatar(Form):
    imagen = ImageField()
        