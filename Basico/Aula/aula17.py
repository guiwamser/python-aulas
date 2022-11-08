from time import sleep

nome = str(input("Digite seu nome: "))
sobreNome = str(input("Digite seu sobreNome: "))
idade = int(input("Digite sua idade: "))
lista_notas = []
situacao = "reprovado"

while situacao != ("aprovado"):
    
    for lista in range(0, 2):
        nota = int(input("Digite sua nota: "))
        lista_notas.append(nota)
        
    media = sum(lista_notas)/ len(lista_notas)

    lista_notas = []

    if media >= 7:
        sleep(2)
        print("*")
        situacao = "aprovado"
        
    
    dicionario_alunos = {"nome":nome, "sobreNome":sobreNome, "idade":idade, "situacao":situacao}
    print(f"{dicionario_alunos['nome']} {dicionario_alunos['sobreNome']} {dicionario_alunos ['idade']} - {dicionario_alunos['situacao']}")    

