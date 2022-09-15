#usando o conceito de importação otimizada  importe a biblioteca que tem a capacidade de gerar um delay na impressão.

#crie uma variável recebendo o conceito de polimorfismo com o sinal de igual.

#crie uma função de impressão usando interpolação e aplique a variável de polimorfismo antes e depois da string cabecalho adicione quebra de linha, ao final.

#usando o conceito de contagem regressiva crie um laco de repeticao que exiba cada número do índice até 20, gere um delay de 2 segundos e imprima uma mensagem de Feliz dia do programador na sua aplicação console.

#crie uma função de impressão usando interpolação e aplique a variável de polimorfismo antes e depois da string utilize como rodapé, definindo o fim do laco de repeticao.

from time import sleep

poli = "="*20

sleep(2)
print(f"\n {poli} CABECALHO {poli} \n")

for cont in range(20, 0, -1):
    print(cont)
    sleep(2)

print("Feliz dia do programador!")

print(f"\n {poli} RODAPE {poli} \n")