from controller import somaSalarios

def menu():
    print("="*15, "CALCULADORA DE SALARIO", "="*15, "\n")
    var = 'sim'
    while var == 'sim':
        n1 = float(input("Digite seu primeiro salario: "))
        n2 = float(input("Digite seu segundo salario: "))
        n3 = float(input("Digite seu terceiro salario: "))
        n4 = float(input("Digite seu quarto salario: "))

        resultado = somaSalarios(n1,n2,n3,n4)
        print("A soma dos salarios é{:.2f}".format(resultado))

        var = input("Voce deseja continuar? \nSim \nNao:>")
        
menu()
print("Voce saiu do programa")