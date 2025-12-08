from comum.crud import *
from comum.utils import *
from tabulate import tabulate
from comum.constantes import *

def fechar_caixa(clientes):
    ID_CLIENTE = 0
    TOTAL_COMPRAS = 1
    print("\nFechamento do caixa")
    print("Data:", obter_data(), "\n")
    total_vendas = 0
    tabela = []
    for cliente in clientes:
        id_cliente = cliente[ID_CLIENTE]
        cliente_obj = buscar_cliente_por_id(id_cliente)
        nome_cliente = cliente_obj.nome if cliente_obj else f"Cliente {id_cliente}"
        total_vendas += cliente[TOTAL_COMPRAS]
        tabela.append([nome_cliente, cliente[TOTAL_COMPRAS]])
    print(tabulate(tabela, headers=["Cliente", "Total"]))
    print("\nTotal de vendas: R$ ", total_vendas, "\n")

def exibir_produtos_sem_estoque():
    print("Produtos sem estoque:")
    produtos = consultar_produtos_sem_estoque()
    for produto in produtos:
        print(produto.nome)
    print()