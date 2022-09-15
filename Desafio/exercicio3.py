# Com base nas aulas passadas vamos criar uma calculadora utilizando o conceito de estrutura de decisão. crie duas variáveis recebendo dados numéricos com casas decimais, a descrição deve ser relacionada com primeira nota e segunda nota! crie uma variável para realizar este cálculo, não esqueça de utilizar o conceito de ordem de procedência aritmética. crie uma função de impressão utilizando polimorfismo e quebra de linhas para definir um cabeçalho para sua aplicação console. utilizando máscara de substituição imprima de forma descritiva a primeira nota, utilize quebra de linha, imprima a segunda nota, utilize a quebra de linha e imprima o resultado. usando estrutura de decisão crie uma condição onde o resultado for maior que sete imprima na sua aplicação console que este aluno está acima da média. usando estrutura de decisão crie uma condição onde o resultado for igual a sete imprima na sua aplicação console que este aluno está na média. usando estrutura de decisão crie uma condição onde o resultado for entre cinco e sete imprima na sua aplicação console que este aluno pode solicitar recuperação. usando estrutura de decisão crie uma condição onde o resultado for entre quatro e cinco imprima na sua aplicação console que este aluno deve procurar o professor. Usando estrutura de decisão crie uma condição de saída e imprima na sua aplicação console que este aluno infelizmente não atingiu o esperado!

n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))

media = (n1 + n2) /2

print("-" * 30, "\n" "Calculadora de média: ", "\n", "-" * 30, "\n")
print("Sua primeira nota foi: {} \n Sua segunda nota foi: {} \n sua media {}".format(n1, n2, media))

if media > 7:
    print("Voce esta acima da media!")
elif media == 7:
    print("Você está na media!")
elif media > 5 < 7:
    print("Você pode solicitar recuperação! :(")
elif media >= 4 == 5:
    print("Você pode procurar ajuda!")
else:
    print("Você não atingiu o esperado! >:(")
