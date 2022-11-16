from conta import Conta

class PessoaFisica(Conta):
    __segundo_titular = ''

    def __init__(self, titular, cpf, saldo_inicial):
        super().__init__(12, 'PF')
        self.__titular = titular
        self.__cpf = cpf
        self.__saldo_inicial = saldo_inicial
        print("Passando pelo construtor da classe pessoa fisica")

    @property
    def segundo_titular(self):
        return self.__segundo_titular

    @segundo_titular.setter
    def segundo_titular(self, segundo_titular):
        self.__segundo_titular = segundo_titular


    def __str__(self):
        return f'{super().__str__}\nTitular:> {self.__titular}\nCPF:> {self.__cpf}\nSaldo inicial:> {self.__saldo_inicial}\nSegundo Titular:> {self.__segundo_titular}'