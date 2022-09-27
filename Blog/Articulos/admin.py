from django.contrib import admin
from Articulos.models import Entrada

# Register your models here.

class entradas_admin(admin.ModelAdmin):
    list_display=("titulo","autor","fecha")
    search_fields=["titulo"]
    list_filter=["autor"]

admin.site.register(Entrada,entradas_admin)