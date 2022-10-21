from controller import salvar, listar

def menu():
    print('*'*20, 'Menu', '*'*20 )

    cond = "sim"
    while cond == "sim":
        Nome= salvar(input("Dite seu nome: "))
        cond = str(input("Deseja Continuar \n sim \n nao \n :> "))

        print("O nome inserido foi {} ". format(Nome))

menu()

print("A lista de Nomes Inseridos\n ", listar ())