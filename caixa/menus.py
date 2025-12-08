from comum.utils import *
from comum.constantes import *

def menu_abrir_caixa():
    while True:
        print("Abrir o caixa:")
        print("[1] - Sim")
        print("[2] - Não")
        opcao = entrar_inteiro("Entre com a opção: ")
        if opcao == ABRIR_CAIXA:
            return True
        elif opcao == NAO_ABRIR_CAIXA:
            return False
        else:
            print("Erro: opção inválida")

def menu_caixa():
    while (True):
        print("\nCaixa aberto")
        print("[1] - Atender cliente")
        print("[2] - Fechar caixa")
        opcao = entrar_inteiro("Entre com a opção: ")
        if opcao in (ATENDER_CLIENTE, FECHAR_CAIXA):
            return opcao
        else:
            print("Erro: opção inválida")

def menu_iniciar_atendimento():
    while (True):
        print("\nDeseja iniciar o atendimento:")
        print("[1] - Sim")
        print("[2] - Não")
        opcao = entrar_inteiro("Entre com a opção: ")
        if opcao == INICIAR_ATENDIMENTO:
            return True
        elif opcao == NAO_INICIAR_ATENDIMENTO:
            return False
        else:
            print("Erro: opção inválida")

def menu_finalizar_atendimento():
    while (True):
        print("\nDeseja finalizar o atendimento:")
        print("[1] - Sim")
        print("[2] - Não")
        opcao = entrar_inteiro("Entre com a opção: ")
        if opcao == FINALIZAR_ATENDIMENTO:
            return True
        elif opcao == NAO_FINALIZAR_ATENDIMENTO:
            return False
        else:
            print("Erro: opção inválida")
