from arquivo import *
from atendimento import *
from encerramento import *
from menus import *

abrir_caixa = menu_abrir_caixa()
if not abrir_caixa:
    exit()
produtos = ler_produtos()
cliente, clientes = 0, []
opcao = menu_caixa()
while opcao != FECHAR_CAIXA:
    cliente, total_compra = atender_cliente(cliente, produtos)
    if total_compra > 0:
        clientes.append([cliente, total_compra])
    opcao = menu_caixa()
if clientes:
    fechar_caixa(clientes)
    exibir_produtos_sem_estoque(produtos)
    gravar_produtos(produtos)
else:
    print("Nenhum cliente atendido.")