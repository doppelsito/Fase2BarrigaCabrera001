from django.db import models
from django.urls import reverse
import uuid

from ckeditor.fields import RichTextField
    
class Genero(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class User(models.Model):
    usuario = models.CharField(max_length=100, null=True, blank=True)
    apellido = models.CharField(max_length=100, blank = False, null = False)
    telefono = models.CharField(max_length=10, null=True, blank=True)
    direccion = models.CharField(max_length=100, null=True, blank=True)
    nacimiento = models.DateField('Nacimiento', null=True, blank=True)

    class Meta: ordering = ['usuario', 'apellido']
    def get_absolute_url(self):return reverse('user_detail', args=[str(self.id)])
    def __str__(self):return f'{self.usuario}, {self.apellido}'

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    autor = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    nombrejuego = models.CharField(max_length=200)
    titulo = models.CharField(max_length=200)
    slug = models.CharField('Slug', max_length = 100, blank = False, null = False)
    genero = models.ManyToManyField(Genero)
    contenido = RichTextField()
    imagen = models.ImageField(null = True, upload_to="post")
    fecha_publicacion = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.titulo

class Analisis(models.Model):
    id = models.AutoField(primary_key=True)
    autor = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    nombrejuego = models.CharField(max_length=200)
    slug = models.CharField('Slug', max_length = 100, blank = False, null = False)
    genero = models.ManyToManyField(Genero)
    contenido = RichTextField()
    puntuacion = models.CharField('Nota del juego (0.1, 1.0)', max_length=3)
    imagen = models.ImageField(null = True, upload_to="analisis")
    fecha_publicacion = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nombrejuego
