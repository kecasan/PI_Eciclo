from django.shortcuts import render
from django.urls import path
from .models import Produto

# Create your views here.
def home(request):
    produtos = Produto.objects.all()
    print(produtos)
    return render(request, 'home.html', {'produtos': produtos})


def carrinho_view(request):
    return render(request, 'carrinho.html')

def lista_produtos(request):
    produtos = Produto.objects.all()
    print(produtos)
    return render(request, 'lista_produtos.html', {'produtos': produtos})

def sobre_view(request):
    return render(request, 'sobre.html')

def visualizar_produto(request):
    return render(request, 'visualizar_produto.html')