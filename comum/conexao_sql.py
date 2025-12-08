from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

BANCO = "banco.db"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, '..', 'dados', BANCO)
DATABASE_URL = f"sqlite:///{os.path.abspath(db_path)}"

engine = create_engine(DATABASE_URL, echo=False, future=True)
SessionLocal = sessionmaker(bind=engine)

def get_session():
    return SessionLocal()

def get_engine():
    return engine
