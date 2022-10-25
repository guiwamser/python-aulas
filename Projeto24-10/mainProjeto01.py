#Crie um programa que leia nome, ano de nascimento e carteira de trabalho de uma pessoa e cadastre-os através 
#de um dicionário em um input , se o número da carteira de trabalho for diferente de ZERO,
#  o dicionário receberá através de uma condicional também os dados do primeiro ano de contratação
#  e o salário. ao final do programa imprima os dados solicitados, esta construção deve ser feita 
# através de funções
from controller import cadastro
def menu():
    print("="*15, "CADASTRO", "="*15, "\n")
    opcao = 1

    while (opcao!=0):
        print("1 -> Fazer Check-in")
        print("2 -> Sair")
 
        opcao = int(input("Opção: "))
        
        match opcao:
            case 1:
                pessoa = {}
                pessoa['Nome'] = str(input('Seu nome: '))
                pessoa['idade'] = int(input('Sua idade: '))
                pessoa['Carteira de trabalho: '] = int(input('Sua carterita de trabalho: '))
                cadastro(pessoa)
                print('Cadastro realizado com sucesso')
        
menu()
