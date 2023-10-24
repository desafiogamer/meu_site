from django.urls import path
from .views import UsuarioCreate
from django.conf import settings
from django.conf.urls.static import static
from .views import perfil, ProfileUpdate
from . import views

urlpatterns = [
    path('registrar/', UsuarioCreate.as_view(),name='registrar'),
    path('perfil-usuario/', views.perfil, name='perfil-usuario'),
    path('profile-update/', ProfileUpdate.as_view(), name='profile-update'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)