# utilizando o conhecimento adquirido crie um documento com namespace conta e nome da classe Conta,
#  conforme orientação de boas práticas.
# Crie o método construtor recebendo atributos , este método deve conter variável de referência de acesso ao 
# objeto, crie os seguintes atributos titular, número, saldo, limite
# Usando __  antes do nome do atributo, torne-os privados sendo assim  os mesmos serão acessíveis apenas na 
# nossa classe.
# Crie métodos set e get para cada atributo  da classe, lembrando que o método set é (definir), e o método get
#  é (pegar), essa condicional é necessária devido os nossos atributos estarem privados.


# -Crie um método str recebendo a variável de referência ao objeto, retorne com um f string, e atribua os
#  métodos get de cada atributo privado da nossa classe. Crie um Documento  com namespace Main a partir do
#  documento conta importe a classe Conta.
# -Crie um objeto de conta e solicite ao usuário a atribuição de valores através de input para cada
# atributo do nosso construtor.
# Crie um print descritivo para nome do titular número da conta e saldo, e usando os métodos get imprima
#  os valores inseridos no nosso objeto, com um novo print realize a impressão de todos os valores dos
# nossos atributos. 
# -Crie um novo objeto conta2 e solicite ao usuário a atribuição de valores, através de input para cada
#  atributo do nosso construtor. 
# Crie um print descritivo para nome do titular número da conta e saldo, e usando os métodos get
#  imprima os valores inseridos no nosso objeto, com um novo print realize a impressão de todos os
#  valores dos nossos atributos de conta2



class Conta:
    def __init__(self,titular,numero,saldo,limite):
        self.__titular = titular
        self.__numero = numero
        self.__saldo = saldo
        self.__limite = limite 

   
    def get_titular(self):
        return self.__titular
    
    def set_titular(self, titular):
        self.__titular = titular

    def get_numero(self):
        return self.__numero

    def set_numero(self, numero):
        self.__numero = numero

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, saldo):
        self.__saldo = saldo 

    def get_limite(self):
        return self.__limite

    def set_limite(self, limite):
        self.__limite = limite
    

    def __str__(self):
        return f'titular{self.get_titular}numero{self.get_numero}saldo{self.get_saldo}limite{self.get_limite}'

