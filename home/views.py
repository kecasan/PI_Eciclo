from django.shortcuts import render, redirect
from .models import Produto, Carrinho
from decimal import Decimal
from django.http import JsonResponse


def adicionar_ao_carrinho(request, produto_id):
    produto = Produto.objects.get(id=produto_id)

    # Verificando o tipo do valor antes de converter
    print(type(produto.preco))  # Deve ser <class 'decimal.Decimal'>

    dados_produto = {
        'nome': produto.nome,
        'preco': float(produto.preco),  # Converte o Decimal para float
        'descricao': produto.descricao,
        'estoque': produto.estoque,
    }

    print(dados_produto)  # Verifica o dicionário completo
    
    return JsonResponse(dados_produto)

# Create your views here.
def home(request):
    from .models import Produto
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
