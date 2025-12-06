from constantes import *
from tabulate import tabulate
from utils import *
from menus import *

def atender_cliente(cliente, produtos):
    if not menu_iniciar_atendimento():
        print("Cliente cancelou o atendimento")
        return 0, 0
    num_item, itens = 0, []
    while True:
        produto = entrar_produto(produtos)
        quantidade = entrar_quantidade(produto)
        if quantidade == 0:
            continue
        num_item += 1
        total_item = quantidade * produto["preco"]
        itens.append([num_item, produto["nome"], quantidade, produto["preco"], total_item])
        produto["quantidade"] -= quantidade
        if menu_finalizar_atendimento():
            break
    cliente += 1
    total_compra = fechar_atendimento(cliente, itens)
    return cliente, total_compra

def fechar_atendimento(cliente, itens):
    TOTAL_ITEM = 4
    id_cliente = f"\nCliente {cliente}"
    print(id_cliente)
    print("Data:", obter_data(), "\n")
    total_compra = 0
    for item in itens:
        total_compra += item[TOTAL_ITEM]
    print(tabulate(itens, headers=['Item', 'Produto', 'Quant.', "Preço", "Total"]))
    print("\nItens:", len(itens))
    print("Total:", total_compra, "\n")
    return total_compra