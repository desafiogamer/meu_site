from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    telefone = models.CharField(max_length=20, null=True)
    imagem = models.ImageField(default='avatar.png', upload_to='midia', verbose_name='Imagem de perfil')

    def __str__(self):
        return f'{self.usuario.username}-Profile'
