import pandas as pd
from modelos import Produto
from conexao_sql import get_session

def banco_produtos_vazio():
    with get_session() as session:
        return session.query(Produto).count() == 0

def atualizar_nome_preco_produtos(csv_path="produtos.csv"):
    df = pd.read_csv(csv_path)
    with get_session() as session:
        for _, row in df.iterrows():
            produto = session.query(Produto).filter_by(nome=row['nome']).first()
            if produto:
                produto.nome = row['nome']
                produto.preco = float(row['preco'])
        session.commit()

def importar_produtos_csv(csv_path="produtos.csv"):
    df = pd.read_csv(csv_path)
    with get_session() as session:
        for _, row in df.iterrows():
            produto = Produto(
                nome=row['nome'],
                quantidade=int(row['quantidade']),
                preco=float(row['preco'])
            )
            session.add(produto)
        session.commit()

def importar_produtos_sustentavel(csv_path="produtos.csv"):
    if banco_produtos_vazio():
        importar_produtos_csv(csv_path)
    else:
        atualizar_nome_preco_produtos(csv_path)