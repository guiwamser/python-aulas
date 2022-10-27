#Faça um programa que tenha uma função chamada contador(),
# A) De 1 até 10, de 1 em 1
# B) De 10 até 0, de 2 em 2
# C) Uma contagem personalizada
from time import sleep

def contador(inicio, fim, passo):
    print("-"*35)

    print(f'Contagem de {inicio} ate {fim}, de {passo} em {passo}')

    for cont in range[inicio, fim, passo]:
        print(cont)

contador('10, 0 ,1')

contador('10, 0, 2')


print('-'*35, "Personalize seu for ", '-'*35)
contador(int(input('inicio: ')), int(input('Fim: ')), int(input('Passo:')))


