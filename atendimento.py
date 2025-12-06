from constantes import *
from tabulate import tabulate
from utils import *
from menus import *
from modelos import *
from crud import *

def atender_cliente(cliente, produtos):
    if not menu_iniciar_atendimento():
        return cliente, [], 0
    num_item, itens = 0, []
    total_compra = 0
    while True:
        produto = entrar_produto(produtos)
        quantidade = entrar_quantidade(produto)
        if quantidade == 0:
            continue
        num_item += 1
        total_item = quantidade * produto.preco
        itens.append([num_item, produto.nome, quantidade, produto.preco, total_item])
        produto.quantidade -= quantidade
        atualizar_produto(produto)
        if menu_finalizar_atendimento():
            break
    for item in itens:
        total_compra += item[2]
    cliente += 1
    return cliente, itens, total_compra

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