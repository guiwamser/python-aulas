from conta import Conta

class PessoaFisica(Conta):
    __segundo_titular = ''

    def __init__(self, titular, cpf, saldo_inicial):
        super().__init__(12, 'pf')
        self.titular = titular
        self.cpf = cpf
        self.saldo_inicial = saldo_inicial

    @property
    def segundo_titular(self):
        return self.__segundo_titular

    @segundo_titular.setter
    def segundo_titular(self, segundo_titular):
        self.__segundo_titular = segundo_titular


    def __str__(self):
        return f'{super().__str__}\nTitular:> {self.titular}\nCPF:> {self.cpf}\nSaldo inicial:> {self.saldo_inicial}\nSegundo Titular:> {self.__segundo_titular}'