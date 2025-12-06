from modelos import Produto
from conexao_sql import conectar, desconectar

def listar_produtos():
    produtos = []
    conn = None
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome, quantidade, preco FROM produto")
        produtos = [Produto(*row) for row in cursor.fetchall()]
    except Exception as ex:
        print(ex)
    finally:
        desconectar(conn)
    return produtos

def atualizar_produto(produto):
    conn = None
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE produto SET nome=?, quantidade=?, preco=? WHERE id=?",
            (produto.nome, produto.quantidade, produto.preco, produto.id)
        )
        conn.commit()
    except Exception as ex:
        print(ex)
    finally:
        desconectar(conn)

def buscar_produto_por_id(id):
    conn = None
    produto = None
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome, quantidade, preco FROM produto WHERE id=?", (id,))
        row = cursor.fetchone()
        if row:
            produto = Produto(*row)
    except Exception as ex:
        print(ex)
    finally:
        desconectar(conn)
    return produto

def consultar_produtos_sem_estoque():
    comando = "select * from produto where quantidade <= 0;"
    produtos = []
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(comando)
        registros = cursor.fetchall()
        for registro in registros:
            id, nome, quantidade, preco = int(registro[0]), registro[1], int(registro[2]), float(registro[3])
            produtos.append(Produto(id, nome, quantidade, preco))
    except Exception as ex:
        print(ex)
    finally:
        desconectar(conn)
    return produtos