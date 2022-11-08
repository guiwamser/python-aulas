DML - data manipulation language
linguagem que permite a manipulação de dados

create table people(
	id int generated always as identity
	,nome varchar(30) not null
	,sobreNome varchar(30) not null
	,idade int null
);


insert into people (
	nome,
	sobrenome,
	idade 	
)
values(
	'Andre'
	,'Boladao'
	,25
);



update people 
	set
		sobrenome = 'Quadros'
	where id = 2

update people 
	set
		sobrenome = 'ABACATE'
	where id >= 1 and id <=6
	

delete from people 
	where id = 3

	
insert into people (nome,sobrenome,idade)
	values('Dieter','Heiss',40);
    