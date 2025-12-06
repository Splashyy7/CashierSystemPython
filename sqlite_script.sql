.open banco.db
.mode table

drop table if exists produto;

create table produto(
	id integer primary key autoincrement,
	nome text not null,
	quantidade int not null,
	preco real not null
);

INSERT INTO produto VALUES (null, 'Produto 1', 1, 10);
INSERT INTO produto VALUES (null, 'Produto 2', 2, 20);
INSERT INTO produto VALUES (null, 'Produto 3', 3, 30);
INSERT INTO produto VALUES (null, 'Produto 4', 4, 40);
INSERT INTO produto VALUES (null, 'Produto 5', 5, 50);