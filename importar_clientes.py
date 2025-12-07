from conexao_sql import get_session, BASE_DIR, engine
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
    if not json_path:
        json_path = os.path.join(BASE_DIR, "clientes.json")
    if os.path.exists(json_path):
        df = pd.read_json(json_path)
        if 'id_cliente' in df.columns:
            df = df.drop(columns=['id_cliente'])
        df.to_sql('cliente', con=engine, if_exists='append', index=False)

def importar_clientes():
    deletar_todos_clientes()
    resetar_autoincremento_cliente()
    importar_clientes_json()