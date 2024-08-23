from django.urls import path
from . import views

urlpatterns = [
    path("finalizar_pedido/", views.finalizar_pedido, name='finalizar_pedido'),
    path("validaCupom/", views.validaCupom, name='validaCupom'),
    path('adicionar_ao_carrinho/<int:produto_id>/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    
    
    ]