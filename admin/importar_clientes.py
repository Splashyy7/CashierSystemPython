from comum.conexao_sql import get_session, BASE_DIR, engine
from sqlalchemy import text
import pandas as pd
import os

def deletar_todos_clientes():
    with get_session() as session:
        session.execute(text("DELETE FROM cliente"))
        session.commit()

def resetar_autoincremento_cliente():
    with engine.connect() as conn:
        conn.execute(text("DELETE FROM sqlite_sequence WHERE name='cliente';"))
        conn.commit()

def importar_clientes_json(json_path=None):
    from comum.modelos import Cliente
    from comum.conexao_sql import get_session, engine, BASE_DIR
    import pandas as pd
    import os
    if not json_path:
        json_path = os.path.join(BASE_DIR, '..', 'dados', "clientes.json")
    json_path = os.path.abspath(json_path)
    if os.path.exists(json_path):
        df = pd.read_json(json_path)
        with get_session() as session:
            for _, row in df.iterrows():
                existe = session.query(Cliente).filter_by(id_cliente=row['id_cliente']).first()
                if not existe:
                    cliente = Cliente(id_cliente=row['id_cliente'], nome=row['nome'])
                    session.add(cliente)
            session.commit()

def importar_clientes():
    deletar_todos_clientes()
    resetar_autoincremento_cliente()
    importar_clientes_json()