from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hamburger', views.HamburgerList.as_view()),
    path('hamburger/', views.HamburgerList.as_view()),
    path('hamburger/<pk>', views.HamburgerDetail.as_view()),
    path('hamburger/<pk>/', views.HamburgerDetail.as_view()),
    path('ingredient', views.IngredientList.as_view()),
    path('ingredient/', views.IngredientList.as_view()),
    path('ingredient/<pk>', views.IngredientDetail.as_view()),
    path('ingredient/<pk>/', views.IngredientDetail.as_view()),
    path('hamburger_ingredient', views.Hamburger_IngredientList.as_view()),
    path('hamburger_ingredient/', views.Hamburger_IngredientList.as_view()),
    path('hamburger_ingredient/<pk>', views.Hamburger_IngredientDetail.as_view()),
    path('hamburger_ingredient/<pk>/', views.Hamburger_IngredientDetail.as_view()),
    path('hamburger/<p_1>/ingredient/<p_2>', views.Hamburger_IngredientDetail.as_view()),
    path('hamburger/<p_1>/ingredient/<p_2>/', views.Hamburger_IngredientDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)


####SLASH APPEND X VER
