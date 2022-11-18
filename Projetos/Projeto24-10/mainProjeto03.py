#Faça um programa que solicite o nome de um aluno solicite também a inserção das últimas três notas este 
# cálculo deve realizar a média desse aluno, e através desta condição deve ser impresso o nome do aluno, 
# as três notas digitadas e a média final, e deve ser impresso se o aluno foi aprovado ou nao!

from controller import resultado


def menu():
    
    
    nome = str(input('Digite seu nome:'))
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a primeira nota: '))
    n3 = float(input('Digite a primeira nota: '))
    n4 = float(input('Digite a primeira nota: '))

    #Variavel Media recebendo funcao resultado
    media = resultado(n1, n2, n3, n4)


    print('-'*35, "Resultado", '-'*35)

    print(f'O Calculo da Media do aluno: {nome} \na primeira nota: {n1} \na segunda nota: {n2} \na terceira nota: {n3} \na quarta nota: {n4} \nO Aluno esta  {media}')



menu()
