.open banco.db
.mode table

DROP TABLE IF EXISTS CLIENTE;
DROP TABLE IF EXISTS PRODUTO;
DROP TABLE IF EXISTS FORNECEDOR;
DROP TABLE IF EXISTS COMPRA;
DROP TABLE IF EXISTS item;
DROP TABLE IF EXISTS FORNECIMENTO;


CREATE TABLE CLIENTE (
    id_cliente INTEGER PRIMARY KEY,
    nome TEXT NOT NULL
);

CREATE TABLE PRODUTO (
    id_produto INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    quantidade INTEGER NOT NULL,
    preco REAL NOT NULL
);

CREATE TABLE FORNECEDOR (
    id_fornecedor INTEGER PRIMARY KEY,
    nome TEXT NOT NULL
);

CREATE TABLE COMPRA (
    id_compra INTEGER PRIMARY KEY,
    data_hora TEXT NOT NULL,
    id_cliente INTEGER NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES CLIENTE(id_cliente)
);

CREATE TABLE item (
    id_item INTEGER PRIMARY KEY AUTOINCREMENT,
    id_compra INTEGER NOT NULL,
    id_produto INTEGER NOT NULL,
    quantidade INTEGER NOT NULL,
    preco REAL NOT NULL,
    FOREIGN KEY (id_compra) REFERENCES compra(id_compra),
    FOREIGN KEY (id_produto) REFERENCES produto(id_produto)
);

CREATE TABLE FORNECIMENTO (
    id_produto INTEGER NOT NULL,
    id_fornecedor INTEGER NOT NULL,
    PRIMARY KEY (id_produto, id_fornecedor),
    FOREIGN KEY (id_produto) REFERENCES PRODUTO(id_produto),
    FOREIGN KEY (id_fornecedor) REFERENCES FORNECEDOR(id_fornecedor)
);