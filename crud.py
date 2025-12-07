from modelos import Produto, Cliente
from conexao_sql import get_session, BASE_DIR
import json
import os

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

def cadastrar_cliente_json(nome_cliente):
    json_path = os.path.join(BASE_DIR, "clientes.json")
    if os.path.exists(json_path):
        with open(json_path, "r", encoding="utf-8") as f:
            clientes = json.load(f)
    else:
        clientes = []
    clientes.append({"nome": nome_cliente})
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(clientes, f, ensure_ascii=False, indent=4)