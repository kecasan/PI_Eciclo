from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=11, blank=True)
    endereco = models.CharField(max_length=100, blank=True)
    telefone = models.CharField(max_length=20, blank=True)
    data_nascimento = models.DateField(blank=True, null=True)
    sexo = models.CharField(max_length=1, blank=True)
    def __str__(self):
        return self.usuario.username
    