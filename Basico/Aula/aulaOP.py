validador = True

validador = False

idade = int(input("Digite sua idade: "))

print(" "*15, "expressão de igualdade", " "*15)


validador = ( idade == 18)
print(validador)

print(" "*15, "expressão de diferenca", " "*15)
validador = ( idade != 18)
print(validador)

print(" "*15, "expressão de maior", " "*15)
validador = ( idade > 18)
print(validador)

print(" "*15, "expressão de menor", " "*15)
validador = ( idade < 18)
print(validador)

print(" "*15, "expressão de maior e igual", " "*15)
validador = ( idade >= 18)
print(validador)

print(" "*15, "expressão de menor e igual", " "*15)
validador = ( idade <= 18)
print(validador)
