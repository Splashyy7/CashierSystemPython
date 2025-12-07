from constantes import *
from utils import *
from menus import *
from modelos import *
from crud import *
import pandas as pd
from tabulate import tabulate

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
        if menu_finalizar_atendimento():
            break
    total_compra = calcular_total_compra(itens)
    return id_cliente, itens, total_compra

def fechar_atendimento(cliente, itens):
    id_cliente = f"\nCliente {cliente}"
    print(id_cliente)
    print("Data:", obter_data(), "\n")
    agrupado = gerar_nota_fiscal_agrupada(itens, return_df=True) 
    for _, row in agrupado.iterrows():
        produto_obj = buscar_produto_por_nome(row['Produto'])
        if produto_obj:
            baixar_estoque(produto_obj, int(row['Quant.']))
    return agrupado['Total'].sum()

def gerar_nota_fiscal_agrupada(itens, return_df=False):
    df = pd.DataFrame(itens, columns=['Item', 'Produto', 'Quant.', 'Preço', 'Total'])
    agrupado = df.groupby(['Produto', 'Preço'], as_index=False).agg({'Quant.': 'sum', 'Total': 'sum'})
    print(tabulate(agrupado, headers='keys', showindex=False))
    print("\nItens:", len(agrupado))
    print("Total:", agrupado['Total'].sum(), "\n")
    if return_df:
        return agrupado