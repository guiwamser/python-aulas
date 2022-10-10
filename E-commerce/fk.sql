alter table compra add constraint compra_fk_funcionario_foreign foreign key (fk_funcionario) 
references funcionarios (id_funcionario);

alter table compra add constraint compra_fk_cliente_foreign foreign key (fk_cliente) 
references cliente (id_cliente);

alter table item add constraint item_fk_compra_foreign foreign key (fk_compra) 
references compra (id_compra);

alter table funcionarios add constraint funcionarios_fk_filial_foreign foreign key (fk_filial) 
references filial (id_filial);