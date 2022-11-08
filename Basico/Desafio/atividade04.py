# 04-EXERCÍCIO: Crie variáveis com tipos predefinidos que suportem a inserção de dados com casas decimais representando os 4 últimos salários de uma (pessoa). crie uma variável para realizar a soma entre estes salários. crie uma função de impressão de dados para definir o cabeçalho de uma calculadora, utilizando o conceito de polimorfismo imprima a palavra Calculadora no centro da sua aplicação console, Logo em seguida use apenas uma vez a função de impressão, descreva cada campo com uma máscara de substituição, Ex " primeira variável : {} " os dados devem ser apresentados um em cada linha na sua aplicação console, deve ser utilizado os caracteres especiais de quebra de linha e na impressão deve apresentar apenas duas casas após a vírgula imprima no final utilizando a variável de soma para imprimir o resultado final do seu exercício.

salarioMaio = float(input("Informe salario Maio: "))
salarioJunho = float(input("Informe salario Junho: "))
salarioJulho = float(input("Informe salario Julho: "))
salarioAgosto = float(input("Informe salario Agosto: "))
somaSalarios = salarioMaio + salarioJunho + salarioJulho + salarioAgosto

print("-" * 10, "calculadora", "-" * 10)
print("Salario Maio: {:.2f},\nSalario Junho: {:.2f},\nSalario Julho: {:.2f},\nSalario Agosto: {:.2f},\nSoma dos salarios: {:.2f}".format(salarioMaio, salarioJunho, salarioJulho, salarioAgosto, somaSalarios))