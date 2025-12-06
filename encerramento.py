from crud import *
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

def exibir_produtos_sem_estoque():
    print("Produtos sem estoque:")
    produtos = consultar_produtos_sem_estoque()
    for produto in produtos:
        print(produto.nome)
    print()