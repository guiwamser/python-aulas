# _   EXERCICIO-01 crie um documento instanciando uma classe chamada Conta com atributos número, titular, 
# saldo, limite crie um método str com a variável  referência que acessa o objeto no espaço alocado de memória, 
# acessando diretamente o objeto de conta. insira os atributos na função através da variável referência padrão,
#  e use f string para adicionar ao return

class Conta:
    numero = 0
    titular = ''
    saldo = 0
    limite = 0

    def __str__(self):
        return f'{self.numero} - {self.titular} - {self.saldo} - {self.limite}'

print(Conta())
