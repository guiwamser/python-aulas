nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
idade = int(input("Idade: "))
salario = float(input("Salario: "))

#formato utilizando o f(format) para definir.

#No Float, as casas decimais serão definidas pela seguinte sintaxe: {:.2f}
#O nome das chaves é {} máscara de substituição
print('Seu nome é: {} {}, você tem {} anos. Salário: {:.2f}'.format(nome, sobrenome, idade, salario))