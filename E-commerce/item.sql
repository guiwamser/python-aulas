create table item(
	id_item int primary key not null,
	valor decimal not null,
	descricao varchar(255) not null,
	fk_compra int null
);