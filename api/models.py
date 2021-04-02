from django.db import models


class Hamburger(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.CharField(max_length=200)
    image = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Hamburger_Ingredient(models.Model):
    id = models.AutoField(primary_key=True)
    id_hamburger = models.IntegerField()
    id_ingredient = models.IntegerField()

    def __str__(self):
        return self.id


class Ingredient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


###AutoField
###IntegerField
