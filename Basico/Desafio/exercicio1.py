# exercício-01 usando a biblioteca interna random use o conceito de importação otimizada de (Escolha (Choice)) de lista , crie quatro variáveis recebendo valores, essas variáveis devem ser com tipos predefinidos tipo string, crie uma variável recebendo uma lista das 4 variáveis, logo em seguida crie outra variável recebendo a importação , essa importação irá realizar o sorteio de um valor recebido. crie uma função de impressão utilizando polimorfismo e quebra de linhas para definir um cabeçalho para sua aplicação console. utilizando a interpolação exiba em seguida com a função de impressão o nome sorteado pela biblioteca random.

from random import choice

n1 = str(input("Digite um funcionário: "))
n2 = str(input("Digite um funcionário: "))
n3 = str(input("Digite um funcionário: "))
n4 = str(input("Digite um funcionário: "))

lista = [n1, n2, n3, n4]

sorteado = choice(lista)

print("-" * 10, "Quem vai limpar o banheiro?", "-" * 10)
print("O funcionario sorteado foi: {}!".format(sorteado))