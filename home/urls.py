from django.urls import path
from home import views


urlpatterns = [
    path("", views.home, name="home"),
    path("carrinho/", views.carrinho_view, name='carrinho'),
]
