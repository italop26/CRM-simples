from django.shortcuts import render
from .models import Produto
from django.http import HttpResponse

def painel_vendedor(request):
    return render(request, 'Vendedor/painel_vendedor.html')

def produtos(request):
    produto = Produto.objects.all()
    return render(request, 'Vendedor/painel_vendedor.html', {'produto': produto})

def tela_registrar_vendas(request):
    produto = Produto.objects.all()
    return render(request, 'Vendedor/Registrar_vendas.html', {'produto': produto})

def registrar_vendas(request, id):
    if request.method == 'POST': 
        produto = Produto.objects.get(id=id)
    if produto.estoque > 0:
        produto.estoque -= 1
        produto.save()
        return HttpResponse ('Registrado com sucesso')
    return render(request, 'Vendedor/painel_vendedor.html')



