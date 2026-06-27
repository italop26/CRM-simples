from django.urls import path
from . import views
from . import views_adm
from . import view_Caixa, view_Estoquista, views_Vendedor

urlpatterns = [ 
    path('', views.login_view),
    
    # Adm
    path('painel_adm/', views_adm.painel_adm, name='painel_adm'),
    path('adicionar_usuario/', views_adm.adicionar_usuario, name='adicionar_usuario'),
    path('adicionar_produto/', views_adm.adicionar_produto, name='adicionar_produto'), 
    path('excluir_usuarios/', views_adm.excluir_usuario, name= 'excluir_usuarios'), 
    path('relatorios/', views_adm.relatorios_atividades, name='relatorios'),
    path('Estoque/', views_adm.estoque, name='estoques'),
    path('usuarios/', views_adm.usuarios, name='usuarios'),

    # Vendedor
    path('painel_vendedor/', views_Vendedor.painel_vendedor, name='painel_vendedor'),
    path('produto/', views_Vendedor.produtos, name='produtos'),
    path('registrar_vendas/<int:id>/', views_Vendedor.registrar_vendas, name='registrar vendas'),
    path('tela_registrar_vendas/', views_Vendedor.tela_registrar_vendas, name='tela_registrar_vendas'),

    # Caixa
    path('painel_caixa/', view_Caixa.painel_caixa, name='painel_caixa'),
    path('registros/', view_Caixa.caixa, name='registro'),

    # Estoquista 
    path('painel_estoquista/', view_Estoquista.painel_estoquista, name='painel_estoquista'),
    path('Estoque_atual/', view_Estoquista.ver_estoque, name='estoques_atual'),
    path('Adicionar_estoque/<int:id>/', view_Estoquista.atualizar_estoques, name='atualizar_estoque')

    ]
