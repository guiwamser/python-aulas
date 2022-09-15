#lista

import random

n1 = str(input("Digite um nome: "))
n2 = str(input("Digite um nome: "))
n3 = str(input("Digite um nome: "))
n4 = str(input("Digite um nome: "))

lista = [n1, n2, n3, n4]

sorteado = random.choice(lista)

print("O nome sorteado foi {}! ".format(sorteado))