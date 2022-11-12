#classe Mãe
class Conta:
    def __init__(self,numero, tipo):
        self.numero = numero
        self.tipo = tipo
        print("Passando pelo construtor conta")

    def __str__(self):
        return f'Numero Conta{self.numero}\nTipo de conta{self.tipo}'

class PessoaFisica(Conta):
    def __init__(self, numero, saldo_inicial):
        
        super().__init__(numero, )
        self.saldo_inicial = saldo_inicial
        print('Passando pela pessoa fisica')

    def __str__(self):
        return f'{super().__str__()\n {self.numero} {self.saldo_inicial}'