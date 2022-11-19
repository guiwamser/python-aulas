from model.pessoaJuridica import PessoaJuridica

def create_pj(conta):
    contas = open('pessoajuridica.txt', 'a')
    contas.write(str(conta)+'\n')
    contas.close()

def read_pj():
    
    lista_contas = []
    contas = open('pessoajuridica.txt', 'r')
    
    for conta in contas:
        conta = conta.strip()
        conta__objeto = conta.split(';')

        print(conta__objeto)

        pessoaJuridica = PessoaJuridica()
        pessoaJuridica.agencia = conta__objeto[0]
        pessoaJuridica.numero_agencia = conta__objeto[1]
        
        pessoaJuridica.titular = conta__objeto[2]
        pessoaJuridica.cnpj = conta__objeto[3]
        pessoaJuridica.saldo_inicial = conta__objeto[4]
        pessoaJuridica.segundo_titular = conta__objeto[5]

        lista_contas.append(pessoaJuridica)

    contas.close
    return lista_contas