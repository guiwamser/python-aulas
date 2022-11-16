from pessoaFisica import PessoaFisica
from pessoaJuridica import PessoaJuridica

pessoaFisica = PessoaFisica('Guilherme', 120349234, 20000)

print('-'*15, 'Menu Pessoa Fisica', '-'*15)
print(pessoaFisica)

print('-'*15, 'Menu segundo titular', '-'*15)

pessoaFisica.segundo_titular = 'Lirinha'
print(pessoaFisica)
