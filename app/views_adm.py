from django.shortcuts import render, redirect
from .models import Produto, Vendedor, Adm, Caixa, Estoquista
from django.http import HttpResponse
from django.contrib import messages
def painel_adm(request):
    return render (request, 'Adm/painel_adm.html')

def adicionar_usuario(request):
    if request.method == 'POST': 

        usuario = request.POST.get('usuario')
        cpf = request.POST.get('cpf')
        idade = request.POST.get('idade')
        senha = request.POST.get('senha')
        cargo = request.POST.get('cargo')

        if cargo == 'adm':
            Adm.objects.create(
                usuario=usuario,
                cpf=cpf,
                idade=idade,
                senha=senha
            )

        elif cargo == 'vendedor':
            Vendedor.objects.create(
                usuario=usuario,
                cpf=cpf,
                idade=idade,
                senha=senha
            )

        elif cargo == 'estoquista':
            Estoquista.objects.create(
                usuario=usuario,
                cpf=cpf,
                idade=idade,
                senha=senha
            )
        elif cargo == 'caixa':
            Caixa.objects.create(
                usuario=usuario,
                cpf=cpf,
                idade=idade,
                senha=senha
            )

            messages.success(request, 'Criado com sucesso')

        return HttpResponse('criado com sucesso')
    return render(request, 'Adm/adicionar_usuario.html')

def adicionar_produto(request):
    if request.method == 'POST':
        nome_produto = request.POST.get('nome_produto')
        preco = request.POST.get('preco')
        estoque = request.POST.get('estoque')
        Produto.objects.create(nome_produto=nome_produto, preco=preco, estoque=estoque)
    
        return HttpResponse('Adicionado com sucesso')
    return render(request, 'Adm/adicionar_produtos.html')


def excluir_usuario(request):

    vendedores = []
    caixas = []
    estoquistas = []

    if request.method == 'POST':

        # Excluir
        if request.POST.get('acao') == 'excluir':

            id = request.POST.get('id')
            cargo = request.POST.get('cargo')

            if cargo == 'vendedor':
                Vendedor.objects.get(id=id).delete()

            elif cargo == 'caixa':
                Caixa.objects.get(id=id).delete()

            elif cargo == 'estoquista':
                Estoquista.objects.get(id=id).delete()

        # Buscar
        elif request.POST.get('acao') == 'buscar':

            busca = request.POST.get('busca')

            vendedores = Vendedor.objects.filter(
                usuario__icontains=busca
            )

            caixas = Caixa.objects.filter(
                usuario__icontains=busca
            )

            estoquistas = Estoquista.objects.filter(
                usuario__icontains=busca
            )

    return render(request, 'Adm/excluir_usuarios.html', {
        'vendedores': vendedores,
        'caixas': caixas,
        'estoquistas': estoquistas
    })
    


def relatorios_atividades(request):
    vendedor = Vendedor.objects.all()
    caixa = Caixa.objects.all()
    estoquista = Estoquista.objects.all()

    return render (request, 'Adm/painel_adm.html', {'vendedor': vendedor, 'caixa': caixa, 'estoquista': estoquista})

def estoque (request):
    produto = Produto.objects.all()

    return render (request, 'Adm/estoque.html', {'produto': produto})

def usuarios(request):
    vendedor = Vendedor.objects.all()
    caixa = Caixa.objects.all()
    estoquista = Estoquista.objects.all()
    return render (request, 'Adm/usuarios.html', {'vendedor': vendedor, 'caixa': caixa, 'estoquista': estoquista})
   