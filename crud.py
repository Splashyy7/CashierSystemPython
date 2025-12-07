from modelos import Produto
from conexao_sql import get_session

def listar_produtos():
    with get_session() as session:
        return session.query(Produto).all()

def atualizar_produto(produto):
    with get_session() as session:
        db_produto = session.query(Produto).filter_by(id=produto.id).first()
        if db_produto:
            db_produto.nome = produto.nome
            db_produto.quantidade = produto.quantidade
            db_produto.preco = produto.preco
            session.commit()

def buscar_produto_por_id(id):
    with get_session() as session:
        return session.query(Produto).filter_by(id=id).first()

def consultar_produtos_sem_estoque():
    with get_session() as session:
        return session.query(Produto).filter(Produto.quantidade <= 0).all()