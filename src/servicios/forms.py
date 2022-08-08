from django.forms import Form, CharField, IntegerField, DateField, BooleanField


class CargaServicio (Form):
    cliente = IntegerField() 
    turno = CharField()
    status = CharField()
    
    