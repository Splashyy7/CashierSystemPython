from admin.menus_admin import (
    menu_principal_sig,
    menu_clientes_sig,
    menu_clientes_com_compras,
    menu_produtos_sig,
    menu_consultas_produtos
)
from admin.consultas_clientes import (
    consultar_compras_cliente,
    consultar_clientes_mais_compram,
    consultar_clientes_mais_gastam,
    consultar_clientes_sem_compras
)
from admin.crud_produtos import (
    listar_produtos,
    cadastrar_produto,
    alterar_produto,
    remover_produto
)
from admin.consultas_produtos import (
    produtos_mais_vendidos,
    produtos_menos_vendidos,
    produtos_pouco_estoque,
    fornecedores_produto
)
from comum.constantes import *

def fluxo_clientes():
    while True:
        opcao = menu_clientes_sig()
        if opcao == MENU_CLIENTES_COMPRAS:
            while True:
                subopcao = menu_clientes_com_compras()
                if subopcao == MENU_CLIENTES_CONSULTAR_COMPRAS:
                    consultar_compras_cliente()
                elif subopcao == MENU_CLIENTES_MAIS_COMPRAM:
                    consultar_clientes_mais_compram()
                elif subopcao == MENU_CLIENTES_MAIS_GASTAM:
                    consultar_clientes_mais_gastam()
                elif subopcao == MENU_CLIENTES_COMPRAS_VOLTAR:
                    break
        elif opcao == MENU_CLIENTES_SEM_COMPRAS:
            consultar_clientes_sem_compras()
        elif opcao == MENU_CLIENTES_VOLTAR:
            break

def fluxo_produtos():
    while True:
        opcao = menu_produtos_sig()
        if opcao == MENU_PRODUTOS_LISTAR:
            listar_produtos()
        elif opcao == MENU_PRODUTOS_CADASTRAR:
            cadastrar_produto()
        elif opcao == MENU_PRODUTOS_ALTERAR:
            alterar_produto()
        elif opcao == MENU_PRODUTOS_REMOVER:
            remover_produto()
        elif opcao == MENU_PRODUTOS_CONSULTAS:
            while True:
                subopcao = menu_consultas_produtos()
                if subopcao == MENU_CONSULTA_MAIS_VENDIDOS:
                    produtos_mais_vendidos()
                elif subopcao == MENU_CONSULTA_MENOS_VENDIDOS:
                    produtos_menos_vendidos()
                elif subopcao == MENU_CONSULTA_POUCO_ESTOQUE:
                    produtos_pouco_estoque()
                elif subopcao == MENU_CONSULTA_FORNECEDORES:
                    fornecedores_produto()
                elif subopcao == MENU_CONSULTA_VOLTAR:
                    break
        elif opcao == MENU_PRODUTOS_VOLTAR:
            break

def main():
    while True:
        opcao = menu_principal_sig()
        if opcao == MENU_SIG_CLIENTES:
            fluxo_clientes()
        elif opcao == MENU_SIG_PRODUTOS:
            fluxo_produtos()
        elif opcao == MENU_SIG_SAIR:
            print("Saindo do SIG.")
            break

if __name__ == "__main__":
    main()