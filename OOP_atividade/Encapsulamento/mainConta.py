from conta import Conta

conta = Conta(input("Digite seu Nome:> "), 
int(input("Digite o numero da sua conta:> ")),
float(input("Digite seu Saldo Inicial:> ")),
float(input("Digite o limite da sua Conta:> ")))

print("A conta do {} de número {} possui um saldo de {}".format(conta.get_titular(),conta.get_numero(),conta.get_saldo()))

