from conta import Conta

class PessoaFisica(Conta):

    __segundo_titular = ''

    def __init__(self, titular, cpf, saldo_inicial):
        self.__titular = titular
        self.__cpf = cpf
        self.__saldo_inicial = saldo_inicial
        super().__init__()

        print('Passando pelo construtor da classe Pessoa Fisica')

    @property
    def __segundo_titular(self):
        return self.__segundo_titular

    @__segundo_titular.setter
    def segundo_titular(self, segundo_titular):
        self.__segundo_titular = segundo_titular

    


        