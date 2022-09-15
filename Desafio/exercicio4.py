# Com base nas aulas passadas vamos criar um sorteio de lista e utilizando o conceito de estrutura de decisão exibir qual foi a posição de ordem de inserção de dados que foi sorteada! usando o conceito de importação otimizada importe a função choice, logo em seguida crie quatro variáveis representadas por nomes n1, n2, n3, n4, essas variáveis devem ser do tipo string e devem solicitar dados. crie uma variável que receba como lista estas quatro variáveis. crie uma variável usando a importação otimizada e atribuindo a variável lista. crie uma função de impressão utilizando polimorfismo e quebra de linhas para definir um cabeçalho para sua aplicação console. utilizando o conceito de interpolação exiba qual foi o nome sorteado. utilizando o conceito de estrutura de decisão cria uma condição que exiba a ordem em que foi digitado o nome sorteado pela variável de sorteio da lista!

from random import choice

n1 = str(input("Digite um nome: "))
n2 = str(input("Digite um nome: "))
n3 = str(input("Digite um nome: "))
n4 = str(input("Digite um nome: "))

lista = [n1, n2, n3, n4]

sorteado = choice(lista)

print("-" * 30, "\n Nome sorteado \n","-" * 30, "\n O nome sorteado foi: {}".format(sorteado))

if sorteado == n1:
    print("Digitado na primeira posição!")
elif sorteado == n2:
    print("Digitado na segunda posição!")
elif sorteado == n3:
    print("Digitado na terceira posição!")
else: 
    print("Digitado na quarta posição!")



