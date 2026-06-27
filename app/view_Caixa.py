from django.shortcuts import render
from django.http import HttpResponse

def painel_caixa(request):
    return render(request, 'Caixa/painel_caixa.html')

saldo_dia = 0

def caixa(request):
    global saldo_dia

    if request.method == 'POST':
        tipo = request.POST.get('tipo')
        valor = float(request.POST.get('valor'))

        if tipo == 'entrada':
            saldo_dia += valor

        elif tipo == 'retirada':
            saldo_dia -= valor

        return HttpResponse('Movimentação registrada')

    contexto = {
        'saldo': saldo_dia
    }

    return render(request, 'Caixa/registros.html', contexto)