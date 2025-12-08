from comum.conexao_sql import get_session
from comum.modelos import Produto, Item, Fornecedor, Fornecimento
from comum.utils import entrar_inteiro
from sqlalchemy import func
from tabulate import tabulate

def produtos_mais_vendidos():
    with get_session() as session:
        resultados = (
            session.query(
                Produto.id_produto,
                Produto.nome,
                func.coalesce(func.sum(Item.quantidade), 0).label('total_vendido')
            )
            .join(Item, Produto.id_produto == Item.id_produto)
            .group_by(Produto.id_produto)
            .order_by(func.sum(Item.quantidade).desc())
            .all()
        )
        print("\nProdutos mais vendidos:")
        print(tabulate(resultados, headers=["ID", "Nome", "Total Vendido"], tablefmt="fancy_grid"))

def produtos_menos_vendidos():
    with get_session() as session:
        resultados = (
            session.query(
                Produto.id_produto,
                Produto.nome,
                func.coalesce(func.sum(Item.quantidade), 0).label('total_vendido')
            )
            .outerjoin(Item, Produto.id_produto == Item.id_produto)
            .group_by(Produto.id_produto)
            .order_by(func.coalesce(func.sum(Item.quantidade), 0))
            .all()
        )
        print("\nProdutos menos vendidos:")
        print(tabulate(resultados, headers=["ID", "Nome", "Total Vendido"], tablefmt="fancy_grid"))

def produtos_pouco_estoque():
    limite = entrar_inteiro("Exibir produtos com estoque menor ou igual a: ")
    with get_session() as session:
        produtos = (
            session.query(Produto)
            .filter(Produto.quantidade <= limite)
            .order_by(Produto.quantidade)
            .all()
        )
        linhas = [[p.id_produto, p.nome, p.quantidade] for p in produtos]
        print("\nProdutos com pouco estoque:")
        print(tabulate(linhas, headers=["ID", "Nome", "Estoque"], tablefmt="fancy_grid"))

def fornecedores_produto():
    id_produto = entrar_inteiro("Digite o ID do produto: ")
    with get_session() as session:
        fornecedores = (
            session.query(Fornecedor)
            .join(Fornecimento, Fornecedor.id_fornecedor == Fornecimento.id_fornecedor)
            .filter(Fornecimento.id_produto == id_produto)
            .all()
        )
        if not fornecedores:
            print("Nenhum fornecedor associado a este produto.")
            return
        linhas = [[f.id_fornecedor, f.nome] for f in fornecedores]
        print("\nFornecedores do produto:")
        print(tabulate(linhas, headers=["ID", "Nome"], tablefmt="fancy_grid"))