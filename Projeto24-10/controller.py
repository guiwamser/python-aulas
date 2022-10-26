def cadastro(pessoa):
    with open('Projeto24-10/projeto.txt', 'a') as arquivo:
        arquivo.write(str(pessoa)+'\n')




def contador(inicio, fim, passo):
    print("-"*35)
    passo = abs(passo) if passo != 0 else 1
