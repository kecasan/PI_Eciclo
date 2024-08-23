from django.urls import path
from home import views


urlpatterns = [
    path("", views.home, name="home"),
    path("carrinho/", views.carrinho_view, name='carrinho'),
    path('produtos/', views.lista_produtos, name='lista_produtos'),
    path("sobre/", views.sobre_view, name='sobre'),
    path('adicionar_ao_carrinho/<int:produto_id>/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    
    ]
