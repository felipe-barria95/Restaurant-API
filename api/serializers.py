from rest_framework import serializers

from .models import Hamburger, Hamburger_Ingredient, Ingredient

class HamburgerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hamburger
        fields = ('id', 'name', 'price', 'description', 'image')

class Hamburger_IngredientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hamburger_Ingredient
        fields = ('id', 'id_hamburger', 'id_ingredient')

class IngredientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'description')
