from conta import Conta

def create(conta):
    contas = open('contas.txt', 'a')
    contas.write(str(conta)+'\n')
    contas.close

def read():

    lista_contas = []
    contas = open('contas.txt', 'r')
    
    for conta in contas:
        conta = conta.strip()
        conta__objeto = conta.split(';')

        print(conta__objeto)

        conta = Conta
        conta.titular = conta__objeto[0]
        conta.numero = conta__objeto[1]
        conta.saldo = conta__objeto[2]

        lista_contas.append(conta)

    contas.close
    return lista_contas


# Função update
def update(conta_update:Conta):
    lista_contas = []
    # Contas abrindo o arquivo txt
    contas = open('contas.txt', 'r')

    for conta in contas:
        conta_limpa = conta.strip()
        conta_objeto = conta_limpa.split(';')

        if conta_update.numero == int(conta_objeto[1]):
            lista_contas.append(str(f'{conta_objeto}\n'))

        else:
            lista_contas.append()

        
    contas.close()
    contas = open('contas.txt', 'a')
    contas.write(str(lista_contas)+'\n')
    contas.close()

# Função delete
def delete(numero_conta):
    lista_contas = []
# Contas abrindo o arquivo txt
    contas = open('contas.txt', 'r')

    for conta in contas:
        conta_limpa = conta.strip()
        conta_objeto = conta_limpa.split(';')

    if numero_conta != int(conta_objeto[1]):
        lista_contas.append(numero_conta)

        contas.close()

    contas = open('contas.txt', 'a')
    contas.write(str(lista_contas))
    contas.close



    

