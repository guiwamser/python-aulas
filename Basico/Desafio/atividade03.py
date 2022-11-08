# 3-EXERCÍCIO: Crie variáveis com tipos predefinidos, utilizando a função de inserção de dados, fica a seu critério a utilização de nomes de variáveis, crie no mínimo 4 variáveis, usando máscara de substituição atribua estas variáveis as suas respectivas descrições


nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
salario = float(input("Digite seu salario: "))
dispensaExercito = bool(input("Você foi dispensado do exercito: "))

print("Nome: {}, idade: {}, salario: {}, dispensaExercito: {}".format(nome, idade, salario, dispensaExercito))