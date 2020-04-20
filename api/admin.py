from django.contrib import admin
from .models import Hamburguesa, Hamburguesa_Ingrediente, Ingrediente

admin.site.register(Hamburguesa)
admin.site.register(Hamburguesa_Ingrediente)
admin.site.register(Ingrediente)
