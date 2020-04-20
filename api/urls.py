from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'hamburguesa', views.HamburguesaViewSet)
router.register(r'hamburguesa_ingrediente', views.Hamburguesa_IngredienteViewSet)
router.register(r'ingrediente', views.IngredienteViewSet)

urlpatterns = [
    path('index/', views.index, name='index'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
