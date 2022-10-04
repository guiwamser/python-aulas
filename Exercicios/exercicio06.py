# Identificador de variavel


digito = (input("Digite a variavel: "))

print(" Existe espaço: {},\n Existe caracter alfabetico: {},\n Existe caracter alfanumerico: {},\n Existe caracter numerico: {}.\n".format(digito.isspace(), digito.isalpha(), digito.isalnum(), digito.isnumeric()))