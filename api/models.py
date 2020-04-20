from django.db import models




class Hamburguesa(models.Model):
    id = models.DecimalField(max_digits=5, decimal_places=0, primary_key=True)
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=5, decimal_places=0)
    descripcion = models.CharField(max_length=200)
    imagen = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Hamburguesa_Ingrediente(models.Model):
    hamburguesa_id = models.DecimalField(max_digits=5, decimal_places=0)
    ingrediente_id = models.DecimalField(max_digits=5, decimal_places=0)

class Ingrediente(models.Model):
    id = models.DecimalField(max_digits=5, decimal_places=0, primary_key=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre



# Create your models here.
