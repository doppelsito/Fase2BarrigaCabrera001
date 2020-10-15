from django.contrib import admin
from . models import Autor, Genero, Noticia

# Register your models here.

admin.site.register(Autor)
admin.site.register(Genero)
admin.site.register(Noticia)