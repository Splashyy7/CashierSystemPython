import os.path
from constantes import *

ARQUIVO = "produtos.csv"
DIR = os.path.dirname(os.path.abspath(__file__))
ARQ = os.path.join(DIR, ARQUIVO)

def ler_produtos():
    produtos = []
    try:
        with open(ARQ, mode="r", encoding="UTF-8") as arquivo:
            for linha in arquivo:
                campos = linha.strip().split(",")
                id = int(campos[ID_DO_PRODUTO])
                nome = campos[NOME]
                quantidade = int(campos[QTD])
                preco = float(campos[PRECO])
                produtos.append({"id": id, "nome": nome, "quantidade": quantidade, "preco": preco})
    except FileNotFoundError:
        print(f"Erro: arquivo {ARQUIVO} não encontrado")
    except (ValueError, IndexError) as ex:
        print(f"Erro ao ler produtos: {ex}")
    return produtos

def gravar_produtos(produtos):
    try:
        with open(ARQ, mode="w", encoding="UTF-8") as arquivo:
            for produto in produtos:
                arquivo.write(f"{produto["id"]},{produto["nome"]},{produto["quantidade"]},{produto["preco"]}\n")
    except Exception as ex:
        print(f"Erro ao gravar produtos: {ex}")