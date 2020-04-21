from .serializers import HamburguesaSerializer, Hamburguesa_IngredienteSerializer, IngredienteSerializer
from .models import Hamburguesa, Hamburguesa_Ingrediente, Ingrediente
from django.http import HttpResponse
from rest_framework import generics

def index(request):
    return HttpResponse("Tarea 2 de Taller de Integración. By: Felipe Barría M.")
# Create your views here.



class HamburguesaList(generics.ListCreateAPIView):
    queryset = Hamburguesa.objects.all()
    serializer_class = HamburguesaSerializer


class HamburguesaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hamburguesa.objects.all()
    serializer_class = HamburguesaSerializer

class IngredienteList(generics.ListCreateAPIView):
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer


class IngredienteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer




#class Hamburguesa_IngredienteViewSet(viewsets.ModelViewSet):
#    queryset = Hamburguesa_Ingrediente.objects.all() ####revisar
#    serializer_class = Hamburguesa_IngredienteSerializer
