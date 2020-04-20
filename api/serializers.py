from rest_framework import serializers

from .models import Hamburguesa, Hamburguesa_Ingrediente, Ingrediente

class HamburguesaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hamburguesa
        fields = ('id', 'nombre', 'precio', 'descripcion', 'imagen')

class Hamburguesa_IngredienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hamburguesa_Ingrediente
        fields = ('id_hamburguesa', 'id_ingrediente')

class IngredienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingrediente
        fields = ('id', 'nombre', 'descripcion')
