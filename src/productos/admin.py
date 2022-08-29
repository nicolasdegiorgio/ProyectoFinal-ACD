from django.contrib import admin
from productos.models import ProductosDetailing,Comentarios #ProductosLimpieza
# Register your models here.

admin.site.register(ProductosDetailing) 
admin.site.register(Comentarios) 
            
#admin.site.register(ProductosLimpieza)             
                
