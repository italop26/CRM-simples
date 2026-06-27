from django.shortcuts import render
from .models import Adm, Vendedor, Caixa, Estoquista
from django.http import HttpResponse

def criar_adm(request):
    adm = Adm.objects.create(
        usuario = 'Admin',
        senha = '12345678',
        is_staff= True
    )
    adm.save()

    return HttpResponse('Admin criado')

def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        admin = Adm.objects.filter(
            usuario=username,
            senha=password
        ).first()

        if admin:
            return render(request, 'Adm/painel_adm.html')

        v = Vendedor.objects.filter(    
        usuario=username,
        senha=password
).first()

        if v:
            return render(request, 'Vendedor/painel_vendedor.html')
        
        caixa = Caixa.objects.filter(
            usuario = username,
            senha = password
        ).first()

        if caixa:
            return render(request, 'Caixa/painel_caixa.html')
        
        estoquista = Estoquista.objects.filter(
            usuario = username,
            senha = password
        ).first()

        if estoquista:
            return render (request, 'Estoquista/painel_estoquista.html')
        
        else:
            return render(
                request,
                'login.html',
                {'erro': 'Usuário ou senha incorretos'}
            )

    else:
        return render(request, 'Adm/login.html')
