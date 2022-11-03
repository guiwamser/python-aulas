#Faça um programa que tenha uma função chamada contador(),
# A) De 1 até 10, de 1 em 1
# B) De 10 até 0, de 2 em 2
# C) Uma contagem personalizada


from controller import contador


def menu():
    print('-' * 35, "Cabecalho Menu", '-' * 35)

    contador(1, 10, 1)
    contador(10, 0, -1)

    print('-' * 35 + f'\n{"PERSONALIZE SUA CONTAGEM"}\n' + '-' * 35)
    
    contador(int(input('Inicio: ')), int(input('Fim: ')), int(input('Passo: ')))

menu()
