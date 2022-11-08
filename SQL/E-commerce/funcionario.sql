create table funcionarios(
	id_funcionario int primary key not null,
	salario decimal not null,
	cargo varchar(15),
	fk_filial int not null
) inherits (pessoa);
