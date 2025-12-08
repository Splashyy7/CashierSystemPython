from comum.modelos import Produto, Cliente, Compra, Item, Fornecedor, Fornecimento
from comum.conexao_sql import get_session, BASE_DIR
import json
import os
from datetime import datetime

def listar_produtos():
    with get_session() as session:
        return session.query(Produto).all()

def atualizar_produto(produto):
    with get_session() as session:
        db_produto = session.query(Produto).filter_by(id_produto=produto.id_produto).first()
        if db_produto:
            db_produto.nome = produto.nome
            db_produto.quantidade = produto.quantidade
            db_produto.preco = produto.preco
            session.commit()

def buscar_produto_por_id(id_produto):
    with get_session() as session:
        return session.query(Produto).filter_by(id_produto=id_produto).first()

def consultar_produtos_sem_estoque():
    with get_session() as session:
        return session.query(Produto).filter(Produto.quantidade <= 0).all()

def buscar_cliente_por_id(id_cliente):
    with get_session() as session:
        return session.query(Cliente).filter_by(id_cliente=id_cliente).first()

def cadastrar_cliente():
    with get_session() as session:
        novo_cliente = Cliente(nome="")
        session.add(novo_cliente)
        session.commit()
        novo_cliente.nome = f"Cliente {novo_cliente.id_cliente}"
        session.commit()
        return novo_cliente.id_cliente, novo_cliente.nome

def cadastrar_cliente_json(id_cliente, nome_cliente):
    json_path = os.path.join(BASE_DIR, '..', 'dados', "clientes.json")
    json_path = os.path.abspath(json_path)
    if os.path.exists(json_path):
        with open(json_path, "r", encoding="utf-8") as f:
            clientes = json.load(f)
    else:
        clientes = []
    clientes.append({"id_cliente": id_cliente, "nome": nome_cliente})
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(clientes, f, ensure_ascii=False, indent=4)

def buscar_produto_por_nome(nome):
    with get_session() as session:
        return session.query(Produto).filter_by(nome=nome).first()

def registrar_compra(id_cliente):
    with get_session() as session:
        nova_compra = Compra(id_cliente=id_cliente, data_hora=datetime.now())
        session.add(nova_compra)
        session.commit()
        return nova_compra.id_compra

def registrar_itens_compra(id_compra, itens_agrupados):
    with get_session() as session:
        for _, row in itens_agrupados.iterrows():
            produto = session.query(Produto).filter_by(nome=row['Produto']).first()
            if produto:
                item = Item(
                    id_compra=id_compra,
                    id_produto=produto.id_produto,
                    quantidade=int(row['Quant.']),
                    preco=float(row['Preço'])
                )
                session.add(item)
        session.commit()

def cadastrar_produto(nome, quantidade, preco):
    with get_session() as session:
        novo_produto = Produto(nome=nome, quantidade=quantidade, preco=preco)
        session.add(novo_produto)
        session.commit()
        return novo_produto

def deletar_produto(produto):
    with get_session() as session:
        db_produto = session.query(Produto).filter_by(id_produto=produto.id_produto).first()
        if db_produto:
            session.delete(db_produto)
            session.commit()

def listar_fornecedores():
    with get_session() as session:
        return session.query(Fornecedor).all()

def cadastrar_fornecimento(id_produto, id_fornecedor):
    with get_session() as session:
        fornecimento = Fornecimento(id_produto=id_produto, id_fornecedor=id_fornecedor)
        session.add(fornecimento)
        session.commit()

def deletar_fornecimentos_produto(id_produto):
    with get_session() as session:
        session.query(Fornecimento).filter_by(id_produto=id_produto).delete()
        session.commit()