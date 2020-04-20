from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import HamburguesaSerializer, Hamburguesa_IngredienteSerializer, IngredienteSerializer
from .models import Hamburguesa, Hamburguesa_Ingrediente, Ingrediente


def index(request):
    return HttpResponse("Tarea 2 de Taller de Integración. By: Felipe Barría M.")
# Create your views here.


class HamburguesaViewSet(viewsets.ModelViewSet):
    queryset = Hamburguesa.objects.all().order_by('id')
    serializer_class = HamburguesaSerializer


class Hamburguesa_IngredienteViewSet(viewsets.ModelViewSet):
    queryset = Hamburguesa_Ingrediente.objects.all() ####revisar
    serializer_class = Hamburguesa_IngredienteSerializer


class IngredienteViewSet(viewsets.ModelViewSet):
    queryset = Ingrediente.objects.all().order_by('id')
    serializer_class = IngredienteSerializer
