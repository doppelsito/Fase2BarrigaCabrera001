from django.urls import path
from . import views
from django.conf.urls import url
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.formularios,name='formulario'),
    path('detallePost/<slug:slug>/', views.detallePost, name='detalle_post'),
    path('analisisPost/<slug:slug>/', views.analisisPost, name = 'analisis_post'),
]