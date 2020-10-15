from django.db import models
from django.urls import reverse 
import uuid 

class Genero(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Noticia(models.Model):

    nombrejuego = models.CharField(max_length=200)
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey('Autor', on_delete=models.SET_NULL, null=True)
    fecha = models.DateField()
    genero = models.ManyToManyField(Genero)
    contenido = models.TextField(help_text='Ingrese contenido de la noticia')

    def __str__(self): # asd
        return self.nombrejuego #asd
 #asd
class Autor(models.Model):

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    fecha_nac = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['nombre', 'apellido']

    def get_absolute_url(self):
        return reverse('autor-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.nombre}, {self.apellido}'
        #asd