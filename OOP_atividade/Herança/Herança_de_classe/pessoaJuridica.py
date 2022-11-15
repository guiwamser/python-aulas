from conta import Conta

class PessoaJuridica(Conta):
    __segundo_titular = ''

    def __init__(self, titular, cnpj, saldo_inicial):
        super().__init__('Guilherme', '1111111111', 10000)
        self.titular = titular
        self.cnpj = cnpj
        self.saldo_inicial = saldo_inicial
        print("Passando pelo construtor da classe pessoa fisica")


    @property
    def segundo_titular(self):
        return self.__segundo_titular

    @segundo_titular.setter
    def segundo_titular(self, segundo_titular):
        self.__segundo_titular = segundo_titular


    def __str__(self, titular, cnpj, saldo_inicial, segundo_titular):
        return f'super().__str__.() Titular:>{titular}\nCPF:>{cnpj}\nSaldo inicial{saldo_inicial}\nSegundo titular{segundo_titular}'
    



