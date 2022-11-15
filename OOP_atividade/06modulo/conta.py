#classe Mãe
class Conta:
    def __init__(self,numero, tipo):
        self.numero = numero
        self.tipo = tipo
        print("Passando pelo construtor conta")

    def __str__(self):
        return f'Numero Conta{self.numero}\nTipo de conta{self.tipo}'

class PessoaFisica(Conta):
    __segundo_titular = ''

    def __init__(self, numero, saldo_inicial):
        
        super().__init__(1030, 'Pessoa fisica' )
        self.saldo_inicial = saldo_inicial
        print('Passando pela pessoa fisica')

    @property 
    def segundo_titular(self):
        return self.__segundo_titular
    @segundo_titular.setter

    def __str__(self):
        return f'{super().__str__()\n {self.numero} {self.saldo_inicial}'