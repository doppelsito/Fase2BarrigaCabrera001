from django.urls import path
from . import views
from django.conf.urls import url
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    path('detallePost/<slug:slug>/', views.detallePost, name='detalle_post'),
    path('analisisPost/<slug:slug>/', views.analisisPost, name='analisis_post'),
    path('user/<int:pk>', views.UserDetailView.as_view(), name = 'user_detail'),
]

urlpatterns += [
    path('crear_usuario',views.UserCreate.as_view(),name='user_form'),
    path('user/<int:pk>/update/',views.UserUpdate.as_view(),name='user_update'),
    path('user/<int:pk>/delete/',views.UserDelete.as_view(),name='user_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
