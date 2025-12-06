from arquivo import *
from utils import *
from tabulate import tabulate
from constantes import *

def fechar_caixa(clientes):
    ID_CLIENTE = 0
    TOTAL_COMPRAS = 1
    print("\nFechamento do caixa")
    print("Data:", obter_data(), "\n")
    total_vendas = 0
    for cliente in clientes:
        cliente[ID_CLIENTE] = "Cliente " + str(cliente[ID_CLIENTE])
        total_vendas += cliente[TOTAL_COMPRAS]
    print(tabulate(clientes, headers=["Cliente", "Total"]))
    print("\nTotal de vendas:", total_vendas, "\n")

def exibir_produtos_sem_estoque(produtos):
    print("Produtos sem estoque:")
    for produto in produtos:
        if produto["quantidade"] <= 0:
            print(produto["nome"])
    print()