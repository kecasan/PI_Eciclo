from django.shortcuts import render, get_object_or_404, redirect
from django.urls import path
from .models import Produto, Carrinho

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

def adicionar_ao_carrinho(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    carrinho, created = Carrinho.objects.get_or_create(usuario=request.user, ativo=True)
    carrinho.produtos.add(produto)
    return redirect('carrinho')