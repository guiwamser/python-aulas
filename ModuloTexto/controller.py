def salvar(nome):
    with open('moduloTexto/pessoas.txt', 'a') as arquivo:
        arquivo.write(f'{nome}\n')

def listar():
    nomes = []
    with open('moduloTexto/pessoas.txt', 'r') as arquivo:
        for name in arquivo:
            name = name.strip()
            nomes.append(name)

    return nomes

#salvar('felipe')
print('Lista nomes', listar())