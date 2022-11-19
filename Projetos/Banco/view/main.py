from model.pessoaFisica import PessoaFisica
from model.pessoaJuridica import PessoaJuridica
from controller.juridico import create_pj, read_pj
from controller.fisico import create_psf, read_psf

def menu():
    menu = 1
    while(menu != 0):
        print("="*30, "Menu Banco", "="*30)
        print("\n[1].Pessoa Fisica \n[2].Pessoa Juridica")
        menu_inical = int(input("Digite o Tipo:"))
        match menu_inical:
            case 1:
                menu = int(input("[1].Criar conta Pessoa Fisica:> \n[2].Listar contas Pessoas Fisicas:> \n[0].sair:> \n"))
                match menu:
                    case 1:
                        pessoaFisica = PessoaFisica()

                        pessoaFisica.titular = input("Digite o Nome do 1° titular:> ")
                        pessoaFisica.cpf = input("Digite seu Cpf:> ")
                        pessoaFisica.saldo_inicial = input("Digite o Saldo Inicial:> ")

                        print("Deseja Cadastrar um Segundo Titular:> \n")
                        cond = 'sim'
                        cond = input('sim ou nao:> ')

                        if cond =='sim':
                            pessoaFisica.segundo_titular = input("Digite o Nome do 2° Titular:> ")

                        create_psf(pessoaFisica)

                    case 2:
                        read_psf()


            case 2:
                menu = int(input("[1].Criar PessoaJuridica:> \n[2].Listar PessoasJuridias:> \n[0].sair:> \n"))
                match menu:
                    case 1:
                        pessoajuridica=PessoaJuridica()

                        pessoajuridica.titular = str(input("Digite o Nome do 1° titular:> "))
                        pessoajuridica.cnpj = input("Digite o Cnpj:> ")
                        pessoajuridica.saldo_inicial = float(input("Digite o Saldo Inicial:> "))

                        print("Deseja Cadastrar um Segundo Titular:> \n")
                        cadastrar=str(input('sim ou nao:> '))
                        if cadastrar=='sim':
                            pessoajuridica.segundo_titular = str(input("Digite o nome do 2° titular: "))
                        create_pj(pessoajuridica)
                         

                    case 2:
                        read_pj()