from django.forms import Form, CharField, IntegerField, EmailField


class CrearUsuario (Form):
    
    nombre = CharField (max_length=50)
    apellido = CharField (max_length=50)
    documento = IntegerField()
    email = EmailField( max_length=254)