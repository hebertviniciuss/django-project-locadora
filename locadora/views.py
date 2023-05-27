from django.shortcuts import render
from locadora.models import Locacao,Filme
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'index.html')

def lista_locacao(request):
    locacoes = Locacao.objects.all()
    return render(request,'locacao.html', {'locacoes': locacoes})

def lista_filmes(request):
    filmes = Filme.objects.all()
    return render(request, 'filmes.html', {'filmes': filmes})