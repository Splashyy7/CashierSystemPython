from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey

Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'cliente'
    id_cliente = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)

    def __str__(self):
        return f"{self.nome} (ID: {self.id_cliente})"

class Produto(Base):
    __tablename__ = 'produto'
    id_produto = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    quantidade = Column(Integer, nullable=False)
    preco = Column(Float, nullable=False)

    def retornar_csv(self) -> str:
        return f"{self.id_produto},{self.nome},{self.quantidade},{self.preco}\n"

    def __str__(self):
        return f"{self.nome} (ID: {self.id_produto}) - {self.quantidade} unidades, R$ {self.preco:.2f}"

class Compra(Base):
    __tablename__ = 'compra'
    id_compra = Column(Integer, primary_key=True, autoincrement=True)
    id_cliente = Column(Integer, ForeignKey('cliente.id_cliente'), nullable=False)
    data_hora = Column(DateTime, nullable=False)

class Item(Base):
    __tablename__ = 'item'
    id_item = Column(Integer, primary_key=True, autoincrement=True)
    id_compra = Column(Integer, ForeignKey('compra.id_compra'), nullable=False)
    id_produto = Column(Integer, ForeignKey('produto.id_produto'), nullable=False)
    quantidade = Column(Integer, nullable=False)
    preco = Column(Float, nullable=False)

class Fornecedor(Base):
    __tablename__ = 'fornecedor'
    id_fornecedor = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)

class Fornecimento(Base):
    __tablename__ = 'fornecimento'
    id_fornecimento = Column(Integer, primary_key=True, autoincrement=True)
    id_produto = Column(Integer, ForeignKey('produto.id_produto'), nullable=False)
    id_fornecedor = Column(Integer, ForeignKey('fornecedor.id_fornecedor'), nullable=False)