from django.contrib import admin
from . models import Genero, Post, Analisis, User
# Register your models here.
admin.site.register(User)
admin.site.register(Genero)
admin.site.register(Post)
admin.site.register(Analisis)