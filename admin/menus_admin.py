from comum.constantes import *
from comum.utils import entrar_inteiro

def menu_principal_sig():
    while True:
        print("\nSIG - Sistema de Informações Gerenciais")
        print(f"[{MENU_SIG_CLIENTES}] - Clientes")
        print(f"[{MENU_SIG_PRODUTOS}] - Produtos")
        print(f"[{MENU_SIG_SAIR}] - Sair")
        opcao = entrar_inteiro("Entre com a opção: ")
        if opcao in (MENU_SIG_CLIENTES, MENU_SIG_PRODUTOS, MENU_SIG_SAIR):
            return opcao
        else:
            print("Erro: opção inválida")

def menu_clientes_sig():
    while True:
        print("\nClientes - SIG")
        print(f"[{MENU_CLIENTES_COMPRAS}] - Clientes com compras")
        print(f"[{MENU_CLIENTES_SEM_COMPRAS}] - Clientes sem compras")
        print(f"[{MENU_CLIENTES_VOLTAR}] - Voltar")
        opcao = entrar_inteiro("Entre com a opção: ")
        if opcao in (MENU_CLIENTES_COMPRAS, MENU_CLIENTES_SEM_COMPRAS, MENU_CLIENTES_VOLTAR):
            return opcao
        else:
            print("Erro: opção inválida")

def menu_clientes_com_compras():
    while True:
        print("\nClientes com compras")
        print(f"[{MENU_CLIENTES_CONSULTAR_COMPRAS}] - Consultar compras de um cliente")
        print(f"[{MENU_CLIENTES_MAIS_COMPRAM}] - Consultar clientes que mais compram")
        print(f"[{MENU_CLIENTES_MAIS_GASTAM}] - Consultar clientes que mais gastam")
        print(f"[{MENU_CLIENTES_COMPRAS_VOLTAR}] - Voltar")
        opcao = entrar_inteiro("Entre com a opção: ")
        if opcao in (MENU_CLIENTES_CONSULTAR_COMPRAS, MENU_CLIENTES_MAIS_COMPRAM, MENU_CLIENTES_MAIS_GASTAM, MENU_CLIENTES_COMPRAS_VOLTAR):
            return opcao
        else:
            print("Erro: opção inválida")

def menu_produtos_sig():
    while True:
        print("\nProdutos - SIG")
        print(f"[{MENU_PRODUTOS_LISTAR}] - Listar produtos")
        print(f"[{MENU_PRODUTOS_CADASTRAR}] - Cadastrar produto")
        print(f"[{MENU_PRODUTOS_ALTERAR}] - Alterar produto")
        print(f"[{MENU_PRODUTOS_REMOVER}] - Remover produto")
        print(f"[{MENU_PRODUTOS_CONSULTAS}] - Consultas")
        print(f"[{MENU_PRODUTOS_VOLTAR}] - Voltar")
        opcao = entrar_inteiro("Entre com a opção: ")
        if opcao in (
            MENU_PRODUTOS_LISTAR, MENU_PRODUTOS_CADASTRAR, MENU_PRODUTOS_ALTERAR,
            MENU_PRODUTOS_REMOVER, MENU_PRODUTOS_CONSULTAS, MENU_PRODUTOS_VOLTAR
        ):
            return opcao
        else:
            print("Erro: opção inválida")

def menu_consultas_produtos():
    while True:
        print("\nConsultas de Produtos")
        print(f"[{MENU_CONSULTA_MAIS_VENDIDOS}] - Produtos mais vendidos")
        print(f"[{MENU_CONSULTA_MENOS_VENDIDOS}] - Produtos menos vendidos")
        print(f"[{MENU_CONSULTA_POUCO_ESTOQUE}] - Produtos com pouco estoque")
        print(f"[{MENU_CONSULTA_FORNECEDORES}] - Fornecedores de um produto")
        print(f"[{MENU_CONSULTA_VOLTAR}] - Voltar")
        opcao = entrar_inteiro("Entre com a opção: ")
        if opcao in (
            MENU_CONSULTA_MAIS_VENDIDOS, MENU_CONSULTA_MENOS_VENDIDOS,
            MENU_CONSULTA_POUCO_ESTOQUE, MENU_CONSULTA_FORNECEDORES, MENU_CONSULTA_VOLTAR
        ):
            return opcao
        else:
            print("Erro: opção inválida")