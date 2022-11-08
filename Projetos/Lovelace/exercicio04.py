# crie uma variável com valor fixo esta variável deve conter um numero que nao interfira na decisão de um índice

# crie uma variável recebendo o conceito de polimorfismo com o sinal de igual.

# crie uma função de impressão usando interpolação e aplique a variável de polimorfismo antes e depois da string cabecalho adicione quebra de linha, ao final.

# crie um laco de repeticao, este laço deve solicitar ao usuário para digitar um número por 3 vezes..

# Dentro do laço, crie a capacidade de soma entre esses números digitados, eles devem ser atributos de soma.

# crie uma função de impressão usando máscara de substituição e imprima de forma descritiva a soma desses números.

# crie uma função de impressão usando interpolação e aplique a variável de polimorfismo antes e depois da string utilize como rodapé, definindo o fim do laço de repetição.

# crie uma função de impressão usando interpolação e aplique a variável de polimorfismo antes e depois da string cabecalho início estrutura de decisão adicione quebra de linha, ao final.

# crie uma estrutura de decisão falando se a soma desses números é maior que 10, menor que 10,  igual a dez, diferente  de 10.

# crie uma função de impressão usando interpolação e aplique a variável de polimorfismo antes e depois da string utilize como rodapé, definindo o fim da estrutura de decisão.



soma=0
a="="*10
print(f"{a}Cabeçalho{a}\n")

for c in range(0,3,1):
    b= int(input("digite um numero: "))
    soma=soma+b

print("A soma entre os valores digitados deu: {}".format(soma))

print(f"{a}Rodapé{a}")

print(f"{a}Cabeçalho{a}\n")

if soma>10:
    print("maior que 10 e diferente de 10")
elif soma==10:
    print("igual a 10 ")
elif soma< 10:
    print("menor que 10 e diferente de 10")

print(f"{a}Rodapé{a}")