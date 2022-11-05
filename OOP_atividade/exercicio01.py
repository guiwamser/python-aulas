# EXERCICIO-01 crie um documento instanciando uma classe chamada conta, crie a função construtor,
#  com a variável referência que acessa os atributos da classe no espaço alocado de memória, 
# acessando diretamente o objeto de conta insira dados internos na função através da variável 
# referência padrão, e insira atributos recebendo valores internos número, titular, saldo, limite.


class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

conta = Conta(123456, "Neymar", 1500, 2000)

print(conta)