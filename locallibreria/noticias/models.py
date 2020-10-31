from django.db import models
from django.urls import reverse
import uuid

#from ckeditor.fields import RichTextField
    
class Genero(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre
        

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    autor = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True)
    nombrejuego = models.CharField(max_length=200)
    titulo = models.CharField(max_length=200)
    slug = models.CharField('Slug', max_length = 100, blank = False, null = False)
    genero = models.ManyToManyField(Genero)
    contenido = models.TextField('Contenido')
    #imagen = models.ImageField(null = True, blank=True)
    fecha_publicacion = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.titulo

class Analisis(models.Model):
    id = models.AutoField(primary_key=True)
    autor = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True)
    nombrejuego = models.CharField(max_length=200)
    slug = models.CharField('Slug', max_length = 100, blank = False, null = False)
    genero = models.ManyToManyField(Genero)
    contenido = models.TextField('Contenido')
    puntuacion = models.CharField('Nota del juego (0.1, 1.0)', max_length=3)
    #imagen = models.ImageField(null = True, blank=True)
    fecha_publicacion = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nombrejuego
