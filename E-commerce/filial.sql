create table filial(
	id_filial int primary key not null,
	estado varchar(25) not null,
	cidade varchar(30) not null,
	cep varchar(8) not null,
	complemento varchar(100) null
);