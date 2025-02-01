from django.contrib import admin
from .models import proveedores, empleados


# Register your models here.
@admin.register(proveedores)
class proveedoresAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'telefono', 'email', 'contacto', 'observaciones')
    search_fields = ('nombre', 'direccion', 'telefono', 'email', 'contacto', 'observaciones')
    list_filter = ('nombre', 'direccion',  'contacto')
    ordering = ('nombre',  'email', 'contacto')

@admin.register(empleados)
class emepleadosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'puesto', 'telefono', 'email', 'direccion', 'fecha_contratacion')
    search_fields = ('nombre', 'puesto', 'telefono', 'email', 'direccion', 'fecha_contratacion')
    list_filter = ('nombre', 'puesto', 'fecha_contratacion')
    ordering = ('fecha_contratacion',)


