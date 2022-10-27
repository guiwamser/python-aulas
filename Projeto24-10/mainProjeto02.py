#Faça um programa que solicite o nome de um aluno solicite também a inserção das últimas três notas este 
# cálculo deve realizar a média desse aluno, e através desta condição deve ser impresso o nome do aluno, 
# as três notas digitadas e a média final, e deve ser impresso se o aluno foi aprovado ou nao!


def Media():

situacao = 'Reprovado'

while situacao == "Reprovado":

    nome = str(input("Digite seu nome: "))
    n1 = int(input("Digite Sua primeira nota: "))
    n2 = int(input("Digite Sua segunda nota: "))
    n3 = int(input("Digite sua terceira nota: "))
    for lista in range(0, 3):
        
        lista_notas = [n1, n2, n3] 
        media = sum(lista_notas)/ len(lista_notas)
    situacao = 'Reprovado Por favor Tente novamente'


    if media >=7:
        situacao = 'PARABENS! VOCE FOI APROVADO'


    dicionario_alunos = {'Nome':nome, 'Lista_Notas': lista_notas, 'Media': media, 'Situacao':situacao}

    #--- Impressão de dados do dicionário através de suas chaves

    print(f"{dicionario_alunos['Nome']}, {dicionario_alunos['Lista_Notas']}, {dicionario_alunos['Media']}, {dicionario_alunos['Situacao']}")




    
print("Voce saiu da sua aplicacao!")

Media()