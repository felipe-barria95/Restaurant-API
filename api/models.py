from django.db import models


class Hamburguesa(models.Model):
    id = models.AutoField(primary_key=True)    ####o decialField puede cambiar
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=5, decimal_places=0)
    descripcion = models.CharField(max_length=200)
    imagen = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Hamburguesa_Ingrediente(models.Model):
    id = models.AutoField(primary_key=True)
    id_hamburguesa = models.DecimalField(max_digits=5, decimal_places=0)
    id_ingrediente = models.DecimalField(max_digits=5, decimal_places=0)


    def __str__(self):
        return self.id


class Ingrediente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre
