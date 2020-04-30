from .serializers import HamburguesaSerializer, Hamburguesa_IngredienteSerializer, IngredienteSerializer
from .models import Hamburguesa, Hamburguesa_Ingrediente, Ingrediente
from django.http import HttpResponse, Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
import json

URL = "https://barria-t02.herokuapp.com/"
URL_LOCAL = "http://127.0.0.1:8000/"
URL_HOST = "https://barria-t02.herokuapp.com/"



def index(request):
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
        try:
            pk = int(pk)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        hamburguesa = self.get_object(pk)
        serializer = HamburguesaSerializer(hamburguesa)
        dict_hamburguesa = serializer.data
        dict_hamburguesa["ingredientes"] = retornar_ingredientes(dict_hamburguesa['id'])
        return Response(dict_hamburguesa)


    def delete(self, request, pk, format=None):
        try:
            pk = int(pk)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        lista_hamburguesas_ingredientes = Hamburguesa_Ingrediente.objects.all()
        serializer2 = Hamburguesa_IngredienteSerializer(lista_hamburguesas_ingredientes, many=True)
        lista = serializer2.data
        for elemento in lista:
            if elemento['id_hamburguesa'] == pk:
                pk_2 = int(elemento['id'])
                hamburguesa_ingrediente = Hamburguesa_Ingrediente.objects.get(pk_2)
                hamburguesa_ingrediente.delete()
        hamburguesa = self.get_object(pk)
        hamburguesa.delete()
        return Response(status=status.HTTP_200_OK)

    def patch(self, request, pk, format=None):
        try:
            pk = int(pk)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = json.loads(request.body)
        hamburguesa = self.get_object(pk)
        for elemento in serializer:
            if elemento == "nombre":
                if type(serializer['nombre']) == str:
                    hamburguesa.nombre = serializer['nombre']
                    hamburguesa.save()
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
            elif elemento == "descripcion":
                if type(serializer['descripcion']) == str:
                    hamburguesa.descripcion = serializer['descripcion']
                    hamburguesa.save()
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
            elif elemento == "imagen":
                if type(serializer['imagen']) == str:
                    hamburguesa.imagen = serializer['imagen']
                    hamburguesa.save()
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
            elif elemento == "precio":
                if type(serializer['precio']) == int:
                    hamburguesa.precio = serializer['precio']
                    hamburguesa.save()
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
            elif elemento == "id":
                return Response(status=status.HTTP_400_BAD_REQUEST)
            elif elemento == "ingredientes":
                return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_200_OK)

class Hamburguesa_IngredienteList(APIView):

    def get(self, request, format=None):
        hamburguesas = Hamburguesa_Ingrediente.objects.all()
        serializer = Hamburguesa_IngredienteSerializer(hamburguesas, many=True)
        return Response(serializer.data)


class Hamburguesa_IngredienteDetail(APIView):

    def get_object(self, pk):
        try:
            return Hamburguesa_Ingrediente.objects.get(pk=pk)
        except Hamburguesa_Ingrediente.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        try:
            pk = int(pk)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        hamburguesa_ingrediente = self.get_object(pk)
        serializer = Hamburguesa_IngredienteSerializer(hamburguesa_ingrediente)
        dict_hamburguesa = serializer.data
        return Response(serializer.data)

    def put(self, request, p_1, p_2, format=None):
        try:
            p_1 = int(p_1)
            p_2 = int(p_2)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        dict_hamburguesa = {"id_hamburguesa": p_1, "id_ingrediente": p_2}
        serializer = Hamburguesa_IngredienteSerializer(data=dict_hamburguesa)

        lista_hamburguesas_ingredientes = Hamburguesa_Ingrediente.objects.all()
        serializer2 = Hamburguesa_IngredienteSerializer(lista_hamburguesas_ingredientes, many=True)
        lista = serializer2.data

        lista_ingredientes =  Ingrediente.objects.all()
        serializer3 = IngredienteSerializer(lista_ingredientes, many=True)
        lista_ingredientes = serializer3.data

        lista_hamburguesas_2 = Hamburguesa.objects.all()
        serializer4 = HamburguesaSerializer(lista_hamburguesas_2, many=True)
        lista_2 = serializer4.data
        if serializer.is_valid():
            i = 0
            j = 0
            for ingrediente in lista_ingredientes:
                if int(ingrediente['id']) == p_2:
                    i+=1
            for hamburguesa in lista_2:
                if int(hamburguesa['id']) == p_1:
                    j+=1
            if i == 0 or j == 0:
                return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
            for elemento in lista:
                if elemento['id_hamburguesa'] == p_1 and elemento['id_ingrediente'] == p_2:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, p_1, p_2, format=None):
        try:
            p_1 = int(p_1)
            p_2 = int(p_2)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        lista_hamburguesas_ingredientes = Hamburguesa_Ingrediente.objects.all()
        serializer2 = Hamburguesa_IngredienteSerializer(lista_hamburguesas_ingredientes, many=True)
        lista = serializer2.data
        for elemento in lista:
            if elemento['id_hamburguesa'] == p_1 and elemento['id_ingrediente'] == p_2:
                pk = elemento['id']
                hamburguesa_ingrediente = self.get_object(pk)
                hamburguesa_ingrediente.delete()
                return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class Hamburguesa_IngredienteList(generics.ListCreateAPIView):
    queryset = Hamburguesa_Ingrediente.objects.all()
    serializer_class = Hamburguesa_IngredienteSerializer

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
        try:
            pk = int(pk)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        ingrediente = self.get_object(pk)
        serializer = IngredienteSerializer(ingrediente)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        try:
            pk = int(pk)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        lista_hamburguesas_ingredientes = Hamburguesa_Ingrediente.objects.all()
        serializer2 = Hamburguesa_IngredienteSerializer(lista_hamburguesas_ingredientes, many=True)
        lista = serializer2.data
        for elemento in lista:
            if elemento['id_ingrediente'] == pk:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        ingrediente = self.get_object(pk)
        ingrediente.delete()
        return Response(status=status.HTTP_200_OK)


def retornar_ingredientes(list_id):
    lista = []
    lista_final = []
    hamburguesas_e_ingredientes = Hamburguesa_Ingrediente.objects.all()
    serializer = Hamburguesa_IngredienteSerializer(hamburguesas_e_ingredientes, many=True)
    for elemento in serializer.data:
        if int(elemento['id_hamburguesa']) == int(list_id):
            lista.append(int(elemento['id_ingrediente']))
    lista.sort()
    for numero in lista:
        dict = {"path" : URL + "ingrediente/{}".format(numero)}
        lista_final.append(dict)
    return lista_final
