from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import redirect

# Create your views here.

###### paginas #######


def css(request):
    return render(request, 'paginas/index.html')

def teste(request):
    return render(request, 'paginas/livros.html')

def config(request):
    return render (request, 'paginas/configurações.html')


######### create ############

#####################

def alterar_senha(request):
    if request.method == "POST":
        form_senha = PasswordChangeForm(request.user, request.POST)
        if form_senha.is_valid():
            user = form_senha.save()
            update_session_auth_hash(request, user)
            return redirect('index')
    else:
        form_senha = PasswordChangeForm(request.user)
    return render(request, 'paginas/alterar-senha.html', {'form_senha': form_senha})

