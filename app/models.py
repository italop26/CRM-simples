from django.db import models
from django.contrib.auth.models import User

class Adm (models.Model):
    usuario = models.CharField(max_length=200)
    idade = models.IntegerField(null=False, blank=True)
    cpf = models.CharField(null=False, unique=True)
    senha = models.CharField(max_length=8, null=True)

class Vendedor(models.Model):
    usuario = models.CharField(max_length=200)
    idade = models.IntegerField(null=False)
    cpf = models.CharField(max_length=11, unique=True)
    senha = models.CharField(max_length=8, null=True)
    vendas = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=0.00)
    horario_trabalho = models.CharField(max_length=100, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return self.usuario.get_full_name()
class Estoquista(models.Model):
    usuario = models.CharField(max_length=200)
    idade = models.IntegerField(null=False)
    cpf = models.CharField(max_length=11, unique=True)
    senha = models.CharField(max_length=8, null=True)
    horario_trabalho = models.CharField(max_length=100, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return self.usuario.get_full_name()
    
class Caixa(models.Model):
    usuario = models.CharField(max_length=200)
    idade = models.IntegerField(null=False)
    cpf = models.CharField(max_length=11, unique=True)
    senha = models.CharField(max_length=8, null=True)    
    horario_trabalho = models.CharField(max_length=100, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return self.usuario.get_full_name()

class Produto(models.Model):
    nome_produto = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField(null=False, default=0)
    
    def __str__(self):
        return self.nome_produto
