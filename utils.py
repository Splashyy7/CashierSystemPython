from constantes import *
from datetime import datetime


def entrar_inteiro(msg):
    while True:
        try:
            num = int(input(msg))
            break
        except:
            print("Erro: valor inválido")
    return num

def entrar_id_produto():
    while True:
        id = entrar_inteiro("Insira o id do produto: ")
        if id > 0:
            break
        else:
            print("Erro: id do produto não pode ser menor que 1")
    return id

def pesquisar_produto(id, produtos):
    while True:
        for produto in produtos:
            if (produto.id == id):
                return produto
        return None

def entrar_produto(produtos):
    while True:
        id = entrar_id_produto()
        produto = pesquisar_produto(id, produtos)
        if produto:
            return produto
        else:
            print("Erro: produto não encontrado")

def verificar_estoque(produto, quantidade):
    if (produto.quantidade >= quantidade):
        return True
    else:
        return False

def entrar_quantidade(produto):
    while True:
        quantidade = entrar_inteiro("Entre com a quantidade: ")
        if quantidade > 0:
            if verificar_estoque(produto, quantidade):
                break
            else:
                print("Erro: produto sem estoque")
                quantidade = 0
                break
        else:
            print("Erro: quantidade inválida")
    return quantidade

def obter_data():
    return datetime.now().strftime('%d/%m/%Y %H:%M')