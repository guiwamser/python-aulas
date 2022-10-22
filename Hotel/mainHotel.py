import datetime
from time import sleep
from controller import checkin, relatorio, procurar, checkout


now = datetime.datetime.now()
hour = now.hour
def menu():
    if hour < 12:
        saudacao = "Bom dia, flor do dia"
    elif hour < 18:
        saudacao = "Boa tarde, forasteiro"
    else:
        saudacao = "Boa noite, meu consagrado"

    print('-'*20, 'HOTEL', '-'*20 )
    print("\n{}!\n".format(saudacao))

    opcao = 1

    while (opcao!=0):
        print("1 -> Fazer Check-in")
        print("2 -> Relatório Hospedes")
        print("3 -> Procurar Hospedes")
        print("4 -> Fazer Check-Out")
        print("5 -> Finalizar Atendimento")
        
        opcao = int(input("Opção: "))
        
        match opcao:
            case 1:
                hospede = {}
                hospede['Nome'] = str(input('Seu nome: '))
                hospede['sobreNome'] = str(input('Seu sobrenome: '))
                hospede['idade'] = int(input('Sua idade: '))
                hospede['cpf'] = int(input('Seu cpf: '))
                checkin(hospede)
            case 2:
                relatorio()
            case 3:
                hospedeFind = str(input("Digite o nome desejado: "))
                procurar(hospedeFind)
            case 4:
                hospedeFind = str(input("Digite o nome desejado: "))
                checkout(hospedeFind)

        
menu()



