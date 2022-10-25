#Faça um programa que tenha uma função chamada contador(),
# A) De 1 até 10, de 1 em 1
# B) De 10 até 0, de 2 em 2
# C) Uma contagem personalizada
from time import sleep

def contador(inicio, fim, passo):
    print("-"*35)
    passo = abs(passo) if passo != 0 else 1
# definindo o passo com o valor absoluto (deixa sinal positivo), e caso seja zero, recebe 1
    print(f'Contagem de {inicio} ate {fim}, de {passo} em {passo}')
    sleep(1.5)

    if inicio <fim:
        for cont in range (inicio, fim +1, passo):
            print (cont, end='')
            sleep(0.3)

    elif inicio > fim:
        for cont in range(inicio, fim-1, passo):
            print(cont, end='')
            sleep(0.3)
        print("Funcionando")

contador(10, 1 ,2)

contador(10, 1, 2)

print('-'*35, "Personalize seu for ", '-'*35)
contador(int(input('inicio: ')), int(input('Fim: ')), int(input('Passo:')))

