from conta import Conta
from controller import create, read, update, delete

conta = Conta()
conta.titular = 'Lucas'
conta.numero = 123456
conta.saldo = 10000000

create(conta)

lista_contas = read()

print(lista_contas)

update(conta)

print('*'*30)

for c in lista_contas:
    print(c)