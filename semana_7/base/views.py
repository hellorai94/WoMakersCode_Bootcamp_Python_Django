from django.shortcuts import render
from django.http import HttpResponse
from base.forms import CadastroForm
from base.models import Cadastro

# Create your views here.
def inicio(request):
    # Para renderizar a página html
    return render(request, 'inicio.html')

def cadastro(request):
    # Pegar informações
    sucesso = False
    form = CadastroForm(request.POST or None)
    if form.is_valid():
        sucesso = True
        form.save()
    contexto = {
        'form': form,
        'sucesso': sucesso
    }
    return render(request, 'cadastro.html', contexto)









