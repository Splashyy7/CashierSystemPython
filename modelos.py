from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()

class Produto(Base):
    __tablename__ = 'produto'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    quantidade = Column(Integer, nullable=False)
    preco = Column(Float, nullable=False)

    def retornar_csv(self) -> str:
        return f"{self.id},{self.nome},{self.quantidade},{self.preco}\n"

    def __str__(self):
        return f"{self.nome} (ID: {self.id}) - {self.quantidade} unidades, R$ {self.preco:.2f}"

class Cliente(Base):
    __tablename__ = 'cliente'

    id_cliente = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)

    def __str__(self):
        return f"{self.nome} (ID: {self.id_cliente})"