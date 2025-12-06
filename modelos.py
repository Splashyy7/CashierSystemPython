from dataclasses import dataclass

@dataclass
class Produto:
    id: int
    nome: str
    quantidade: int
    preco: float

    def retornar_csv(self) -> str:
        return f"{self.id},{self.nome},{self.quantidade},{self.preco}\n"

    def __str__(self):
        return f"{self.nome} (ID: {self.id}) - {self.quantidade} unidades, R$ {self.preco:.2f}"