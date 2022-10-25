def cadastro(pessoa):
    with open('Projeto24-10/projeto.txt', 'a') as arquivo:
        arquivo.write(str(pessoa)+'\n')
