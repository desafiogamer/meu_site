from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .forms import Usuarioforms
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Profile

# Create your views here.

def perfil(request):
    return render(request, 'perfil-usuario.html')

class UsuarioCreate(CreateView):
    form_class = Usuarioforms
    template_name = 'registros.html'
    success_url = reverse_lazy ('login')

    def form_valid(self, form):
        url = super().form_valid(form)
        Profile.objects.create(usuario=self.object)

        return url
        
class ProfileUpdate(UpdateView):
    model = Profile
    fields = ['nome', 'email', 'telefone', 'imagem']
    template_name = 'profile.html'
    success_url = reverse_lazy('perfil-usuario')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Profile, usuario=self.request.user)
        return self.object
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Meus dados pessoais'
        context['botao'] = 'Atualizar'

        return context