from django.shortcuts import render
from .models import *
from django.views import generic
from django.utils import timezone
from .models import Post, Analisis
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.core.paginator import Paginator
# Create your views here.
def index(request):

    num_noticias=Post.objects.all().count()
    num_users=User.objects.all().count()
    posts = Post.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('-fecha_publicacion')
    postsAnalisis = Analisis.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('-fecha_publicacion')

    #paginacion
    paginator = Paginator(posts,5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    paginatorAnalisis = Paginator(postsAnalisis,5)
    pageAnalisis = request.GET.get('page')
    postsAnalisis = paginatorAnalisis.get_page(page)

    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(request,'index.html',{'num_noticias':num_noticias,'num_users':num_users,'posts': posts, 'postsAnalisis': postsAnalisis})

def detallePost(request,slug):
    num_noticias=Post.objects.all().count()
    num_users=User.objects.all().count()
    posts = Post.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('-fecha_publicacion')

    post = Post.objects.get(
        slug = slug
    )
    print(post)
    return render(request,'reportaje.html',{'detalle_post':post, 'num_noticias':num_noticias,'num_users':num_users,'posts': posts})

def formularios(request):
    return render(request,'formulario.html')

def analisisPost(request,slug):
    posts = Analisis.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('-fecha_publicacion')

    post = Analisis.objects.get(
        slug = slug
    )
    print(post)
    return render(request,'juego.html',{'analisis_post':post, 'posts': posts})


