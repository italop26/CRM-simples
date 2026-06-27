from django.shortcuts import render
from .models import Produto
from django.http import HttpResponse

def painel_estoquista(request):
    return render(request, 'Estoquista/painel_estoquista.html')

def ver_estoque(request):
    estoques = Produto.objects.all()
    return render(request, 'Estoquista/painel_estoquista.html', {'estoques': estoques})

def atualizar_estoques(request, id):
    produto = Produto.objects.get(id=id)

    if request.method == 'POST':
        estoque = int(request.POST.get('estoque'))
        produto.estoque += estoque
        produto.save()

        return HttpResponse('Adicionado com sucesso')

    return render(
        request,
        'Estoquista/atualizar_estoque.html',
        {'produto': produto}
    )


    