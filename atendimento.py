from constantes import *
from tabulate import tabulate
from utils import *
from menus import *
from modelos import *
from crud import *

def baixar_estoque(produto, quantidade):
    produto.quantidade -= quantidade
    atualizar_produto(produto)

def calcular_total_compra(itens):
    TOTAL_ITEM = 4
    return sum(item[TOTAL_ITEM] for item in itens)

def atender_cliente(produtos):
    id_cliente = int(input("Digite o id do cliente: "))
    cliente_obj = buscar_cliente_por_id(id_cliente)
    if not cliente_obj:
        print("Cliente não cadastrado. Cadastrando novo cliente...")
        id_cliente, nome_cliente = cadastrar_cliente()
        cadastrar_cliente_json(nome_cliente)
        print(f"Cliente cadastrado: {nome_cliente} (ID: {id_cliente})")
    else:
        id_cliente = cliente_obj.id_cliente
    if not menu_iniciar_atendimento():
        return id_cliente, [], 0
    num_item, itens = 0, []
    while True:
        produto = entrar_produto(produtos)
        quantidade = entrar_quantidade(produto)
        if quantidade == 0:
            continue
        num_item += 1
        total_item = quantidade * produto.preco
        itens.append([num_item, produto.nome, quantidade, produto.preco, total_item])
        baixar_estoque(produto, quantidade)
        if menu_finalizar_atendimento():
            break
    total_compra = calcular_total_compra(itens)
    return id_cliente, itens, total_compra

def fechar_atendimento(cliente, itens):
    id_cliente = f"\nCliente {cliente}"
    print(id_cliente)
    print("Data:", obter_data(), "\n")
    print(tabulate(itens, headers=['Item', 'Produto', 'Quant.', "Preço", "Total"]))
    print("\nItens:", len(itens))
    total_compra = calcular_total_compra(itens)
    print("Total:", total_compra, "\n")
    return total_compra