from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os.path

BANCO = "banco.db"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BANCO = os.path.join(BASE_DIR, BANCO)

def conectar():
    try:
        engine = create_engine("sqlite:///" + BANCO)
        session = sessionmaker(bind=engine)()
    except Exception as ex:
        print(ex)
        exit()
    return session

def desconectar(session):
    if (session):
        session.close()