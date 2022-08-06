from django.forms import Form, CharField, IntegerField, FloatField


class CargaProducto (Form):
    nombre = CharField(max_length=150)
    marca = CharField(max_length=150)
    precio = FloatField()
    tipo = CharField(max_length=20) #Todavia no se le da mucha utilidad
    stock = IntegerField()
    
    
class FormularioBusqueda(Form):
    
    nombre_producto = CharField(max_length=150)