from .serializers import HamburgerSerializer, Hamburger_IngredientSerializer, IngredientSerializer
from .models import Hamburger, Hamburger_Ingredient, Ingredient
from django.http import HttpResponse, Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
import json

URL = "https://barria-t02.herokuapp.com/"
URL_LOCAL = "http://127.0.0.1:8000/"
URL_HOST = "https://barria-t02.herokuapp.com/"



def index(request):
    return HttpResponse("Restaurant API by: Felipe Barría M. For more information visit: https://github.com/felipe-barria95/Restaurant-API")
# Create your views here.


class HamburgerList(APIView):

    def get(self, request, format=None):
        hamburgers = Hamburger.objects.all()
        serializer = HamburgerSerializer(hamburgers, many=True)
        final_list = []
        for element in serializer.data:
            element["ingredient"] = return_ingredients(element['id'])
            final_list.append(element)
        return Response(final_list)

    def post(self, request, format=None):
        serializer = HamburgerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            hamburger_dict = serializer.data
            hamburger_dict['ingredients'] = []
            return Response(hamburger_dict, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class HamburgerDetail(APIView):

    def get_object(self, pk):
        try:
            return Hamburger.objects.get(pk=pk)
        except Hamburger.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        try:
            pk = int(pk)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        hamburger = self.get_object(pk)
        serializer = HamburgerSerializer(hamburger)
        hamburger_dict = serializer.data
        hamburger_dict["ingredients"] = return_ingredients(hamburger_dict['id'])
        return Response(hamburger_dict)


    def delete(self, request, pk, format=None):
        try:
            pk = int(pk)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        hamburger_ingredient_list = Hamburger_Ingredient.objects.all()
        serializer = Hamburger_IngredientSerializer(hamburger_ingredient_list, many=True)
        list = serializer.data
        for element in list:
            if element['id_hamburger'] == pk:
                pk_2 = int(element['id'])
                hamburger_ingredient = Hamburger_Ingredient.objects.get(id=pk_2)
                hamburger_ingredient.delete()
        hamburger = self.get_object(pk)
        hamburger.delete()
        return Response(status=status.HTTP_200_OK)

    def patch(self, request, pk, format=None):
        try:
            pk = int(pk)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = json.loads(request.body)
        hamburger = self.get_object(pk)
        for element in serializer:
            if element == "name":
                if type(serializer['name']) == str:
                    hamburger.name = serializer['name']
                    hamburger.save()
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
            elif element == "description":
                if type(serializer['description']) == str:
                    hamburger.descritcion = serializer['description']
                    hamburger.save()
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
            elif elemento == "image":
                if type(serializer['image']) == str:
                    hamburger.image = serializer['image']
                    hamburger.save()
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
            elif elemento == "price":
                if type(serializer['price']) == int:
                    hamburger.price = serializer['price']
                    hamburger.save()
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        hamburger = self.get_object(pk)
        serializer = HamburgerSerializer(hamburger)
        hamburger_dict = serializer.data
        hamburger_dict["ingredient"] = return_ingredients(hamburger_dict['id'])
        return Response(hamburger_dict, status=status.HTTP_200_OK)

class Hamburger_IngredientList(APIView):

    def get(self, request, format=None):
        hamburger = Hamburger_Ingredient.objects.all()
        serializer = Hamburger_IngredientSerializer(hamburger, many=True)
        return Response(serializer.data)


class Hamburger_IngredientDetail(APIView):

    def get_object(self, pk):
        try:
            return Hamburger_Ingredient.objects.get(pk=pk)
        except Hamburger_Ingredient.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        try:
            pk = int(pk)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        hamburger_ingredient = self.get_object(pk)
        serializer = Hamburger_IngredientSerializer(hamburger_ingredient)
        hamburger_dict = serializer.data
        return Response(serializer.data)

    def put(self, request, p_1, p_2, format=None):
        try:
            p_1 = int(p_1)
            p_2 = int(p_2)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        hamburger_dict = {"id_hamburger": p_1, "id_ingredient": p_2}
        serializer = Hamburger_IngredientSerializer(data=hamburger_dict)

        hamburger_ingredient_list = Hamburger_Ingredient.objects.all()
        serializer2 = Hamburger_IngredientSerializer(hamburger_ingredient_list, many=True)
        lista = serializer2.data

        ingredient_list =  Ingredient.objects.all()
        serializer3 = IngredientSerializer(ingrediente_list, many=True)
        ingredient_list = serializer3.data

        hamburguesas_list_2 = Hamburger.objects.all()
        serializer4 = HamburgerSerializer(hamburguesas_list_2, many=True)
        list_2 = serializer4.data
        if serializer.is_valid():
            i = 0
            j = 0
            for ingredient in ingredient_list:
                if int(ingredient['id']) == p_2:
                    i+=1
            for hamburger in lista_2:
                if int(hamburger['id']) == p_1:
                    j+=1
            if i == 0 or j == 0:
                return Response(status=status.HTTP_404_NOT_FOUND)
            for element in list:
                if element['id_hamburguer'] == p_1 and element['id_ingredient'] == p_2:
                    return Response(status=status.HTTP_200_OK) ##aca es
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, p_1, p_2, format=None):
        try:
            p_1 = int(p_1)
            p_2 = int(p_2)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        hamburger_ingredient_list = Hamburger_Ingredient.objects.all()
        serializer2 = Hamburger_IngredientSerializer(hamburger_ingredient_list, many=True)
        list = serializer2.data
        for element in list:
            if element['id_hamburger'] == p_1 and element['id_ingredient'] == p_2:
                pk = element['id']
                hamburger_ingredient = self.get_object(pk)
                hamburger_ingredient.delete()
                return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)


class Hamburger_IngredientList(generics.ListCreateAPIView):
    queryset = Hamburger_Ingredient.objects.all()
    serializer_class = Hamburger_IngredientSerializer

class IngredientList(generics.ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class IngredientDetail(APIView):

    def get_object(self, pk):
        try:
            return Ingredient.objects.get(pk=pk)
        except Ingrediente.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        try:
            pk = int(pk)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        ingredient = self.get_object(pk)
        serializer = IngredientSerializer(ingrediente)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        try:
            pk = int(pk)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        hamburger_ingredient_list = Hamburger_Ingredient.objects.all()
        serializer2 = Hamburger_IngredientSerializer(hamburger_ingredient_list, many=True)
        list = serializer2.data
        for element in list:
            if element['id_ingredient'] == pk:
                return Response(status=status.HTTP_409_CONFLICT)
        ingredient = self.get_object(pk)
        ingredient.delete()
        return Response(status=status.HTTP_200_OK)


def return_ingredients(_id):
    list = []
    final_list = []
    hamburger_ingredient = Hamburger_Ingredient.objects.all()
    serializer = Hamburger_IngredientSerializer(hamburger_ingredient, many=True)
    for element in serializer.data:
        if int(element['id_hamburger']) == int(_id):
            list.append(int(element['id_ingredient']))
    list.sort()
    for number in list:
        dict = {"path" : URL + "ingredient/{}".format(number)}
        final_list.append(dict)
    return final_list
