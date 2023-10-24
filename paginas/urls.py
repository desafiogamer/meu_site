from django.contrib import admin
from django.urls import path
from .views import css, teste, config, alterar_senha
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.css, name='index'),
    path('livros/', views.teste, name='livros'),
    path('config/', views.config, name='config'),
    path('alterar_senha/', alterar_senha, name='alterar_senha'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)