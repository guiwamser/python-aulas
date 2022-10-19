CREATE TABLE "pessoa"(
    "nome" VARCHAR(255) NOT NULL,
    "idade" INTEGER NOT NULL,
    "cpf" VARCHAR(255) NOT NULL,
    "endereco" VARCHAR(255) NOT NULL
);

CREATE TABLE "reu"(
    "id_reu" INTEGER NOT null generated always as identity,
    "menor_21" BOOLEAN NOT NULL,
    "passagem_policia" BOOLEAN NOT NULL,
    "negativo" BOOLEAN NOT NULL,
    "fk_advogado" INTEGER NOT NULL
)inherits(pessoa);

ALTER TABLE
    "reu" ADD PRIMARY KEY("id_reu");
   
   
CREATE TABLE "advogado"(
    "id_advogado" INTEGER NOT null generated always as identity,
    "oab" INTEGER NOT NULL,
    "uf" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "advogado" ADD PRIMARY KEY("id_advogado");
   
ALTER TABLE
    "advogado" ADD CONSTRAINT "advogado_oab_unique" UNIQUE("oab");
   
   
   
CREATE TABLE "peticao"(
    "id_peticao" INTEGER NOT null generated always as identity,
    "dt_emissao" DATE NOT NULL,
    "valor" DOUBLE PRECISION NOT NULL,
    "fk_reu" INTEGER NOT NULL,
    "fk_autor" INTEGER NOT NULL
);
ALTER TABLE
    "peticao" ADD PRIMARY KEY("id_peticao");
   
   
CREATE TABLE "autor"(
    "id_autor" INTEGER NOT null generated always as identity,
    "provas" VARCHAR(255) NOT NULL,
    "extra_judicial" BOOLEAN NOT NULL,
    "artigo_lesado" VARCHAR(255) NOT NULL,
    "fk_advogado" INTEGER NOT NULL
)inherits(pessoa);



ALTER TABLE
    "autor" ADD PRIMARY KEY("id_autor");
   
   
   
CREATE TABLE "peticao_direito"(
    "id" INTEGER NOT null generated always as identity,
    "fk_direito" INTEGER NOT NULL,
    "fk_peticao" INTEGER NOT NULL
);
ALTER TABLE
    "peticao_direito" ADD PRIMARY KEY("id");
   
   
   
CREATE TABLE "direito_trabalista"(
    "id_direito" INTEGER NOT null generated always as identity,
    "descricao" TEXT NOT NULL,
    "capitulo" VARCHAR(255) NOT NULL,
    "secao" VARCHAR(255) NOT NULL,
    "artigo" VARCHAR(255) NOT NULL
);

ALTER TABLE
    "direito_trabalista" ADD PRIMARY KEY("id_direito");
   
   
ALTER TABLE
    "direito_trabalista" ADD CONSTRAINT "direito_trabalista_artigo_unique" UNIQUE("artigo");
   
   
ALTER TABLE
    "peticao_direito" ADD CONSTRAINT "peticao_direito_fk_direito_foreign" FOREIGN KEY("fk_direito") REFERENCES "direito_trabalista"("id_direito");
ALTER TABLE
    "peticao" ADD CONSTRAINT "peticao_fk_autor_foreign" FOREIGN KEY("fk_autor") REFERENCES "autor"("id_autor");
ALTER TABLE
    "autor" ADD CONSTRAINT "autor_fk_advogado_foreign" FOREIGN KEY("fk_advogado") REFERENCES "advogado"("id_advogado");
ALTER TABLE
    "peticao" ADD CONSTRAINT "peticao_fk_reu_foreign" FOREIGN KEY("fk_reu") REFERENCES "reu"("id_reu");
ALTER TABLE
    "reu" ADD CONSTRAINT "reu_fk_advogado_foreign" FOREIGN KEY("fk_advogado") REFERENCES "advogado"("id_advogado");
ALTER TABLE
    "peticao_direito" ADD CONSTRAINT "peticao_direito_fk_peticao_foreign" FOREIGN KEY("fk_peticao") REFERENCES "peticao"("id_peticao");
    
   
insert into advogado (
	oab,
	uf 
)
values(
	12345678,
	'mato grosso do sul'
);

insert into advogado (
	oab,
	uf 
)
values(
	12345679,
	'Santa Catarina'
);


insert into direito_trabalista (
	descricao,
	capitulo,
	artigo,
	secao
)
values(
	'As Carteiras de Trabalho e Previdência Social serão entregues aos interessados
pessoalmente, mediante recibo.',
	'1',
	'25',
	'3'
)


insert into autor (
	nome,
	idade,
	cpf,
	endereco,
	provas,
	extra_judicial,
	artigo_lesado,
	fk_advogado 
)
values(
	'Dieter',
	'22',
	'12345678901',
	'Rua das Capivaras',
	'Roubo',
	true,
	true,
	1
)

insert into reu (
	nome,
	idade,
	cpf,
	endereco,
	menor_21,
	passagem_policia,
	negativo,
	fk_advogado 
)
values(
	'Nicolas',
	'171',
	'12345678900',
	'Rua dos Jaguaras',
	true,
	true,
	true,
	2
)

insert into peticao (
	dt_emissao,
	valor,
	fk_reu,
	fk_autor
) values
(
	'2022-10-17',
	2000,
	1,
	1
)


insert into peticao_direito (
	fk_direito,
	fk_peticao 
)
values(
	1,
	1
)