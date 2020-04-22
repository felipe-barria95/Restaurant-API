from .serializers import HamburguesaSerializer, Hamburguesa_IngredienteSerializer, IngredienteSerializer
from .models import Hamburguesa, Hamburguesa_Ingrediente, Ingrediente
from django.http import HttpResponse, Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics

URL = "https://barria-t02.herokuapp.com/"
URL_LOCAL = "http://127.0.0.1:8000/"
URL_HOST = "https://barria-t02.herokuapp.com/"



def index(request):
    print("hola")
    return HttpResponse("Tarea 2 de Taller de Integración. By: Felipe Barría M.")
# Create your views here.


class HamburguesaList(APIView):

    def get(self, request, format=None):
        hamburguesas = Hamburguesa.objects.all()
        serializer = HamburguesaSerializer(hamburguesas, many=True)
        lista_final = []
        for elemento in serializer.data:
            elemento["ingredientes"] = retornar_ingredientes(elemento['id'])
            lista_final.append(elemento)
        return Response(lista_final)

    def post(self, request, format=None):
        serializer = HamburguesaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HamburguesaDetail(APIView):

    def get_object(self, pk):
        try:
            return Hamburguesa.objects.get(pk=pk)
        except Hamburguesa.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        hamburguesa = self.get_object(pk)
        print(hamburguesa)
        serializer = HamburguesaSerializer(hamburguesa)
        dict_hamburguesa = serializer.data
        dict_hamburguesa["ingredientes"] = retornar_ingredientes(dict_hamburguesa['id'])
        return Response(dict_hamburguesa)


    def delete(self, request, pk, format=None):
        hamburguesa = self.get_object(pk)
        hamburguesa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Hamburguesa_IngredienteList(generics.ListCreateAPIView):
    queryset = Hamburguesa_Ingrediente.objects.all()
    serializer_class = Hamburguesa_IngredienteSerializer

class Hamburguesa_IngredienteDetail(APIView):

    def get_object(self, pk):
        try:
            return Hamburguesa_Ingrediente.objects.get(pk=pk)
        except Hamburguesa_Ingrediente.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        hamburguesa_ingrediente = self.get_object(pk)
        serializer = Hamburguesa_IngredienteSerializer(hamburguesa_ingrediente)
        dict_hamburguesa = serializer.data
        return Response(serializer.data)

    def put(self, request, p_1, p_2, format=None):
        dict_hamburguesa = {"id_hamburguesa": p_1, "id_ingrediente": p_2}
        serializer = Hamburguesa_IngredienteSerializer(data=dict_hamburguesa)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        hamburguesa = self.get_object(pk)
        hamburguesa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class IngredienteList(generics.ListCreateAPIView):
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer

class IngredienteDetail(APIView):

    def get_object(self, pk):
        try:
            return Ingrediente.objects.get(pk=pk)
        except Ingrediente.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        ingrediente = self.get_object(pk)
        serializer = IngredienteSerializer(ingrediente)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        hamburguesa = self.get_object(pk)
        hamburguesa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def retornar_ingredientes(list_id):
    lista = []
    hamburguesas_e_ingredientes = Hamburguesa_Ingrediente.objects.all()
    serializer = Hamburguesa_IngredienteSerializer(hamburguesas_e_ingredientes, many=True)
    for elemento in serializer.data:
        if int(elemento['id_hamburguesa']) == int(list_id):
            dict = {"path" : URL + "ingrediente/{}".format(elemento['id_ingrediente'])}
            lista.append(dict)
    return lista
