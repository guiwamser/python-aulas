# EXERCICIO-02 crie um documento instanciando uma classe chamada conta, crie a função construtor, 
# com a variável referência que acessa os atributos da classe no espaço alocado de memória, 
# defina os atributos diretamente na função construtor número, titular, saldo, limite, 
# crie um segundo documento main com variável conta 1, conta 2, conta 3 , 
# insira valores diferentes para cada objeto, imprima no terminal o espaço  
# alocado de memória do objeto principal , e de cada variável de referência para o objeto!

class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular 
        self.saldo = saldo
        self.limite = limite
