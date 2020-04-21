from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hamburguesa/', views.HamburguesaList.as_view()),
    path('ingrediente/', views.IngredienteList.as_view()),
    path('hamburguesa/<int:pk>/', views.HamburguesaDetail.as_view()),
    path('ingrediente/<int:pk>/', views.IngredienteDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
