nome = str(input("Digite seu nome: "))
sobreNome = str(input("Digite seu sobrenome: "))
nomeCompleto = nome + " " + sobreNome
idade = int(input("Digite sua idade: "))

print(f"nome: {nome} {sobreNome} \nidade: {idade}", type(nome), type(sobreNome), type(idade))
print("Seu nome {} \n sua idade {} ".format(nomeCompleto.title(), idade))