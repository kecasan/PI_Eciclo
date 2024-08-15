from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def carrinho_view(request):
    return render(request, 'carrinho.html')

def sobre_view(request):
    return render(request, 'sobre.html')