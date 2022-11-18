from datetime import date

# Caso possua Carteira de Trabalho entra na funcao de validacao
def validacao(dados):
    #condicional if recebendo a variavel de atributo da funcao 
    # se a pessoa possuir carteira de trabalho e numero digitado for diferente de 0 entra nas seguintes condicionais
     if dados['ctps'] > 0:
        dados['contratação'] = int(input('ANO DE CONTRATAÇÃO: '))
        dados['salário'] = float(input('SALÁRIO: R$'))
        dados['aposentadoria'] = dados['contratação'] - (date.today().year - dados['idade']) + 35

# Mostrando os dados pessoais na tela
def impressao(dados):
    
    print('-' * 25 + f'\n{"DADOS PESSOAIS":^25}\n' + '-' * 25)
    
    for chave, valor in dados.items():
        print(f'{chave}: {valor}')



from time import sleep

#Funcao de contador recebendo atributos por padrao
def contador(inicio, fim, passo):

    print('-' * 35)
    #abs()função retorna o valor absoluto do número fornecido.
    passo = abs(passo) if passo != 0 else 1 
    #print descritivo recebendo os passos defindos 
    print(f'Contagem de {inicio} até {fim}, de {passo} em {passo}')

    #funcao interna sleep
    sleep(0.5)

    #estrutura condicional se o inicio for menor que o final a condicao sera incremental
    if inicio < fim:
        print("Contador Incremental")
        #Contador Incremental
        #for recebendo variavel defindindo as sequencias dos passos executado
        for cont in range(inicio, fim + 1, passo):
            #Print recebendo variavel cont do for, e end para impresao dos passos lado a lado
            print(cont, end=' ')
            sleep(0.3)

    #estrutura condicional se o inicio for maior que o final a condicao sera decremental
    elif inicio > fim:
        print("Contador decremental")
        #Contador Decremental 
        #variavel definida recebendo condicao de contagem de decremento
        for cont in range(inicio, fim - 1, -passo):
            #Print recebendo variavel cont do for, e end para impresao dos passos lado a lado
            print(cont, end=' ')
            sleep(0.3)
    #Print De Saida Do bloco
    print('Final...')


def resultado(n1, n2, n3, n4):

    media = (n1 + n2+ n3+ n4) / 4

    if media >= 7:
        media = 'Aprovado'

    elif media >= 5:
        media = 'Recuperação'

    else:
        media = 'Reprovado'
    return media