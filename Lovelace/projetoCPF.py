from time import sleep
import os


poli = "*"*10
nome = ''
telefone = 0
cpf = 0
escolha=False
cont =0
usuario = {"nome":nome, "telefone":telefone, "cpf":cpf}
banco = []

sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')
while escolha == False:
    
    escolha2 =False
    escolha3 =False
    cond=False
    s = str(input("\nVocê gostaria de se identificar? \n sim \n nao \n cadastro \n :>"))

    if s == "sim":
        os.system('cls' if os.name == 'nt' else 'clear')
        id=str(input("digite seu nome: "))
        if id in banco:
                print("tem cad")
                usuario['nome']=id
                usuario['telefone']=telefone
                usuario['cpf']=cpf
        else:
                print("n tem") 
                print(f"\n {poli} IDENTIFIQUE-SE {poli} \n")

                nome = str(input("Digite seu nome completo: ")) 

                telefone = int(input("Digite o número do seu telefone: "))

                cpf = int(input("Digite o seu CPF: "))
                banco.append(nome)
                usuario['nome']=id
                usuario['telefone']=telefone
                usuario['cpf']=cpf
                sleep(2)
                
        final = "Obrigado {} pelo contato!! Tenha um otimo dia!".format(usuario['nome'])
        while escolha2==False:
            sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Escolha a opção:\n1.Reclamção\n2.Alteração de dados\n")
            var=int(input("digite a opção aqui:"))
            if(var==1):
                
                os.system('cls' if os.name == 'nt' else 'clear')
                relato = str(input("Por favor, nos relate o ocorrido: "))
                
                print(final)
                while cond == False:
                    t=str(input("\nGostaria de falar com um de nossos atendentes? \n sim \n nao \n :>"))
                    if  t== "sim":
                        
                        os.system('cls' if os.name == 'nt' else 'clear')
                        for c in range(10,0,-1):
                            sleep(2)
                            print("Por favor aguarde, estamos direcionando para um de nossos atendentes \n posição na fila: {} de 10".format(c))
                        print("Encaminhado!!")
                        sleep(2)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        cond=True
                        escolha2=True
                    elif t == "nao": 
                        print(final)
                        sleep(2)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        cond=True
                        escolha2=True
                        
                    else:
                        cond = False
                        print("Condição inexistente")
                        sleep(2)
                        os.system('cls' if os.name == 'nt' else 'clear')
            elif var==2:
                print("escolheu 2")
                os.system('cls' if os.name == 'nt' else 'clear')
                while(escolha3==False):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Escolha a opção:\n1.Nome \n2.CPF\n3.Telefone")
                    var=int(input("digite a opção aqui:"))
                    if(var==1):
                        print("escolheu alteração de nome")
                        nome=str(input("Digite o novo nome:"))
                        usuario["nome"]=nome
                        print("seu nome foi alterado para: {}".format(usuario["nome"]))
                        print("obrigado {} pelo contato!".format(usuario["nome"]))
                        sleep(2)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        escolha3=True
                        escolha2=True
                    elif var ==2:
                        print("escolheu alteração de cpf")
                        sleep(2)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        cpf = str(input("Digite um CPF válido (somente números):"))
                        if len(cpf) == 11:
                            #entra nas outras validações
                            validacao1 = False    
                            #Primeira validação
                            resultado = 0
                            c = 10
                            for i in range(9):
                                resultado = resultado+(int(cpf[i])*c)
                                
                                c = c-1
                            #print(f"Total das multiplicações primera parte:{resultado}")
                            
                            resultado = (resultado*10)%11
                            if resultado == 10:
                                resultado = 0
                            
                            #print(f"Resto da divisão: {resultado} tem que ser igual a {cpf[9]}")
                            
                            if resultado == int(cpf[9]):
                                validacao1 = True
                                
                            #print(f"Resto da divisão: {(resultado*10)%11}")
                            
                            #print("Primeira Validação correta")
                            #=============
                            #Segunda validação
                            validacao2 = False
                            resultado = 0
                            c = 11
                            for i in range(10):
                                resultado = resultado+(int(cpf[i])*c)
                                
                                c = c-1
                            
                            #print(f"Total das multiplicações segunda parte:{resultado}")
                            
                            resultado = (resultado*10)%11
                            
                            #print(f"Resto da divisão: {resultado} tem que ser igual a {cpf[10]}")
                            
                            if resultado == int(cpf[10]):
                                validacao2 = True
                            

                            
                            #print(f"Resultado: {validacao1} {validacao2}")
                            
                            if validacao1 and validacao2:
                                print("CPF Válido")
                                escolha2=True
                                escolha3=True
                                usuario["cpf"]=cpf
                                print("seu cpf foi alterado para: {}".format(usuario["cpf"]))
                                print(final)
                                sleep(2)
                                os.system('cls' if os.name == 'nt' else 'clear')
                            else:
                                print("CPF Inválido")
                                escolha2=True
                                escolha3=True
                                print(final)
                                sleep(2)
                                os.system('cls' if os.name == 'nt' else 'clear')
                        else:
                            print("CPF inválido")
                            escolha2=True
                            escolha3=True
                            print(final)
                            sleep(2)
                            os.system('cls' if os.name == 'nt' else 'clear')
                    elif var ==3:
                            
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("escolheu alteração de telefone")
                            telefone=str(input("Digite o novo telefone:"))
                            usuario["telefone"]=telefone
                            print("seu telefone foi alterado para: {}".format(usuario["telefone"]))
                            print(final)
                            sleep(2)
                            os.system('cls' if os.name == 'nt' else 'clear')
                            escolha2=True
                            escolha3=True
                    else:
                            print("valor digitado incorreto \n")
                            sleep(2)
                            os.system('cls' if os.name == 'nt' else 'clear')
                            escolha3=False
            else:
                print("valor digitado incorreto \n")
                sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                escolha2=False



    elif s == "nao": 
        
        relato = str(input("Por favor, nos relate o ocorrido: "))
        print("Obrigado por relatar!")
        sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
    elif s=="cadastro":
        print(f"\n {poli} IDENTIFIQUE-SE {poli} \n")

        nome = str(input("Digite seu nome completo: ")) 

        telefone = int(input("Digite o número do seu telefone: "))

        cpf = int(input("Digite o seu CPF: "))
        banco.append(nome)
        
        sleep(2)
    else:
        print("Condição inexistente")
        sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')