from controller import soma
from controller import somaSalarios

poli = "*"*20

print(f"\n {poli} CARCULADORA {poli}")


salarioJulho = float(input("Informe seu salario de Julho: "))
salarioAgosto = float(input("Informe seu salario de Agosto: "))
salarioSetembro = float(input("Informe seu salario de Setembro: "))
salarioOutubro = float(input("Informe seu salario de Outubro: "))

print (somaSalarios(salarioJulho, salarioAgosto, salarioSetembro, salarioOutubro))



