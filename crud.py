from modelos import Produto
from conexao_sql import conectar, desconectar

def listar_produtos():
    session = None
    produtos = []
    try:
        session = conectar()
        produtos = session.query(Produto).all()
    except Exception as ex:
        print(ex)
    finally:
        desconectar(session)
    return produtos

def atualizar_produto(produto):
    session = None
    try:
        session = conectar()
        db_produto = session.query(Produto).filter_by(id=produto.id).first()
        if db_produto:
            db_produto.nome = produto.nome
            db_produto.quantidade = produto.quantidade
            db_produto.preco = produto.preco
            session.commit()
    except Exception as ex:
        print(ex)
    finally:
        desconectar(session)

def buscar_produto_por_id(id):
    session = None
    produto = None
    try:
        session = conectar()
        produto = session.query(Produto).filter_by(id=id).first()
    except Exception as ex:
        print(ex)
    finally:
        desconectar(session)
    return produto

def consultar_produtos_sem_estoque():
    session = None
    produtos = []
    try:
        session = conectar()
        produtos = session.query(Produto).filter(Produto.quantidade <= 0).all()
    except Exception as ex:
        print(ex)
    finally:
        desconectar(session)
    return produtos