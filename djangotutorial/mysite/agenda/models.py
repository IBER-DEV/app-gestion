from django.db import models
PUESTO_CHOICES = [
                ('Gerente', 'Gerente'),
                ('Asistente', 'Asistente'),
                ('Operador', 'Operador'),
                ('Administrativo', 'Administrativo'),
            ]



# Create your models here.

class proveedores(models.Model):
    nombre = models.CharField(max_length=50, blank=False, null=False)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    contacto = models.CharField(max_length=50, blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)

    

class empleados(models.Model):
            nombre = models.CharField(max_length=50, blank=False, null=False)
            puesto = models.CharField(max_length=50,blank=False, null=False)
            puesto = models.CharField(max_length=50, choices=PUESTO_CHOICES,default='Gerente', blank=False, null=False)
            telefono = models.CharField(max_length=50, blank=True, null=True)
            email = models.EmailField(max_length=50, blank=True, null=True)
            direccion = models.CharField(max_length=100, blank=True, null=True)
            fecha_contratacion = models.DateField(blank=True, null=True)

    



