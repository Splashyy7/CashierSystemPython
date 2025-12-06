import sqlite3
import os.path

BANCO = "banco.db"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, BANCO)

def verificar_db():
    if (not os.path.exists(db_path)):
        print("Erro: banco não encontrado")
        exit()

def conectar():
    conn = None
    try:
        conn = sqlite3.connect(db_path)
    except Exception as ex:
        print(ex)
    return conn
    
def desconectar(conn):
    if (conn):
        conn.close()