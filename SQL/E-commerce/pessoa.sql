CREATE table pessoa(
	nm_completo varchar(80) not null,
	email varchar(30) not null,
	cpf varchar(11) not null,
	dt_nascimento date null,
	senha varchar(30) not null
);
alter table pessoa add constraint pessoa_cpf_unique unique (cpf)