.open banco.db
.mode table

drop table if exists produto;

create table produto(
	id integer primary key autoincrement,
	nome text not null,
	quantidade int not null,
	preco real not null
);


drop table if exists cliente;

create table cliente(
	id_cliente integer primary key autoincrement,
	nome text not null
);