from comum.crud import buscar_cliente_por_id
from comum.conexao_sql import get_session
from comum.modelos import Cliente, Compra, Item, Produto
from sqlalchemy import func
from tabulate import tabulate

def consultar_compras_cliente():
    id_cliente = int(input("Digite o ID do cliente: "))
    with get_session() as session:
        compras = (
            session.query(Compra)
            .filter_by(id_cliente=id_cliente)
            .order_by(Compra.data_hora.desc())
            .all()
        )
        if not compras:
            print("Nenhuma compra encontrada para este cliente.")
            return
        print("\nCompras do cliente (mais recentes primeiro):")
        for compra in compras:
            print(f"\nCompra {compra.id_compra} - Data/Hora: {compra.data_hora}")
            itens = (
                session.query(Item, Produto)
                .join(Produto, Item.id_produto == Produto.id_produto)
                .filter(Item.id_compra == compra.id_compra)
                .all()
            )
            tabela = [
                [produto.nome, item.quantidade, item.preco, item.quantidade * item.preco]
                for item, produto in itens
            ]
            print(tabulate(tabela, headers=["Produto", "Quantidade", "Preço", "Total"]))


def consultar_clientes_mais_compram():
    with get_session() as session:
        resultados = (
            session.query(
                Cliente.id_cliente,
                Cliente.nome,
                func.count(Compra.id_compra).label('num_compras')
            )
            .join(Compra, Cliente.id_cliente == Compra.id_cliente)
            .group_by(Cliente.id_cliente)
            .order_by(func.count(Compra.id_compra).desc())
            .all()
        )
        print(tabulate(resultados, headers=["ID", "Nome", "Nº Compras"]))


def consultar_clientes_mais_gastam():
    with get_session() as session:
        resultados = (
            session.query(
                Cliente.id_cliente,
                Cliente.nome,
                func.coalesce(func.sum(Item.quantidade * Item.preco), 0).label('total_gasto')
            )
            .join(Compra, Cliente.id_cliente == Compra.id_cliente)
            .join(Item, Compra.id_compra == Item.id_compra)
            .group_by(Cliente.id_cliente)
            .order_by(func.sum(Item.quantidade * Item.preco).desc())
            .all()
        )
        print(tabulate(resultados, headers=["ID", "Nome", "Total Gasto"]))


def consultar_clientes_sem_compras():
    with get_session() as session:
        subquery = session.query(Compra.id_cliente).distinct()
        clientes = (
            session.query(Cliente)
            .filter(~Cliente.id_cliente.in_(subquery))
            .all()
        )
        tabela = [[cliente.id_cliente, cliente.nome] for cliente in clientes]
        print(tabulate(tabela, headers=["ID", "Nome"]))