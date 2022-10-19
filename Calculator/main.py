from controller import soma
from controller import subtracao
from controller import multiplicacao
from controller import divisao



poli = "*"*20
print(f"\n {poli} CARCULADORA {poli}")

opcao = 1

while opcao:
    print("0. Sair")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicação")
    print("4. Divisão ")

    opcao = int(input("Opção: "))
    
    if(opcao==1):
        soma()
    if(opcao==2):
        subtracao()
    if(opcao==3):
        multiplicacao()
    if(opcao==4):
        divisao()