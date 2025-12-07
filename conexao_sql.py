from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
import pandas as pd

BANCO = "banco.db"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, BANCO)
DATABASE_URL = f"sqlite:///{db_path}"

engine = create_engine(DATABASE_URL, echo=False, future=True)
SessionLocal = sessionmaker(bind=engine)

def get_session():
    return SessionLocal()

def carregar_clientes_json():
    json_path = os.path.join(BASE_DIR, "clientes.json")
    if os.path.exists(json_path):
        df = pd.read_json(json_path)
        df.to_sql('cliente', con=engine, if_exists='replace', index=False)