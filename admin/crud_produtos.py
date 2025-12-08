from comum.crud import (
    listar_produtos as crud_listar_produtos,
    buscar_produto_por_id,
    cadastrar_produto as crud_cadastrar_produto,
    atualizar_produto as crud_atualizar_produto,
    deletar_produto as crud_deletar_produto,
    listar_fornecedores,
    cadastrar_fornecimento,
    deletar_fornecimentos_produto
)
from comum.utils import entrar_inteiro, entrar_float, entrar_texto
from tabulate import tabulate

def listar_produtos():
    produtos = crud_listar_produtos()
    print("\nLISTA DE PRODUTOS")
    if not produtos:
        print("Nenhum produto cadastrado.")
        return
    linhas = []
    for p in produtos:
        linhas.append([p.id_produto, p.nome, p.quantidade, f"R$ {p.preco:.2f}"])
    print(tabulate(linhas, headers=["ID", "Produto", "Estoque", "Preço"], tablefmt="fancy_grid"))

def cadastrar_produto():
    print("\nCADASTRAR PRODUTO")
    nome = entrar_texto("Nome do produto: ")
    quantidade = entrar_inteiro("Quantidade inicial: ")
    preco = entrar_float("Preço: ")
    novo_produto = crud_cadastrar_produto(nome, quantidade, preco)
    print(f"Produto cadastrado com ID {novo_produto.id_produto}.")
    associar_fornecedores(novo_produto.id_produto)

def alterar_produto():
    print("\nALTERAR PRODUTO")
    id_produto = entrar_inteiro("ID do produto a alterar: ")
    produto = buscar_produto_por_id(id_produto)
    if not produto:
        print("Produto não encontrado.")
        return
    print(f"Alterando produto: {produto.nome}")
    nome = entrar_texto(f"Novo nome [{produto.nome}]: ") or produto.nome
    quantidade = entrar_inteiro(f"Nova quantidade [{produto.quantidade}]: ") or produto.quantidade
    preco = entrar_float(f"Novo preço [{produto.preco}]: ") or produto.preco
    crud_atualizar_produto(produto, nome, quantidade, preco)
    print("Produto alterado com sucesso.")
    associar_fornecedores(id_produto)

def remover_produto():
    print("\nREMOVER PRODUTO")
    id_produto = entrar_inteiro("ID do produto a remover: ")
    produto = buscar_produto_por_id(id_produto)
    if not produto:
        print("Produto não encontrado.")
        return
    
    if crud_deletar_produto(produto):
        deletar_fornecimentos_produto(id_produto)
        print("Produto removido com sucesso.")
    else:
        print("Não é possível remover este produto porque já existem vendas registradas com ele.")

def associar_fornecedores(id_produto):
    fornecedores = listar_fornecedores()
    if not fornecedores:
        print("Nenhum fornecedor cadastrado.")
        return
    print("Fornecedores disponíveis:")
    linhas = [[f.id_fornecedor, f.nome] for f in fornecedores]
    print(tabulate(linhas, headers=["ID", "Nome"], tablefmt="fancy_grid"))
    ids = input("Digite os IDs dos fornecedores para associar (separados por vírgula): ")
    id_list = [int(i.strip()) for i in ids.split(",") if i.strip().isdigit()]
    deletar_fornecimentos_produto(id_produto)
    for id_fornecedor in id_list:
        cadastrar_fornecimento(id_produto, id_fornecedor)
    print("Associação de fornecedores atualizada.")