from django.contrib import admin
from clientes.models import Avatar, Usuarios

# Register your models here.
admin.site.register(Usuarios)  
admin.site.register(Avatar)