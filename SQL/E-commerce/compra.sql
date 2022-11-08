create table compra(
	id_compra int primary key not null,
	dt_compra date not null,
	dt_pagamento date null,
	valor_total decimal not null,
	forma_pagamento varchar(30) not null,
	fk_funcionario int not null,
	fk_cliente int not null
);