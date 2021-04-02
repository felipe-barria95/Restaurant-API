from django.contrib import admin
from .models import Hamburger, Hamburger_Ingredient, Ingredient

admin.site.register(Hamburger)
admin.site.register(Hamburger_Ingredient)
admin.site.register(Ingredient)
