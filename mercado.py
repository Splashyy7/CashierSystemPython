from scraping_produtos import scrape_produtos_url
from crud import *
from atendimento import *
from encerramento import *
from menus import *
from importar_produtos import importar_produtos_sustentavel
from importar_clientes import importar_clientes

scrape_produtos_url("https://pedrovncs.github.io/lindosprecos/produtos.html#")
importar_produtos_sustentavel()
importar_clientes()

abrir_caixa = menu_abrir_caixa()
if not abrir_caixa:
    exit()
produtos = listar_produtos()
cliente, clientes = 0, []
opcao = menu_caixa()
while opcao != FECHAR_CAIXA:
    id_cliente, itens, total_compra = atender_cliente(produtos)
    if total_compra > 0:
        fechar_atendimento(id_cliente, itens)
        clientes.append([id_cliente, total_compra])
    opcao = menu_caixa()
if clientes:
    fechar_caixa(clientes)
    exibir_produtos_sem_estoque()
else:
    print("Nenhum cliente atendido.")