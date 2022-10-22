def checkin(hospede):
    with open('Hotel/hotel.txt', 'a') as arquivo:
        arquivo.write(str(hospede)+'\n')

def relatorio():
    with open('Hotel/hotel.txt', 'r') as arquivo:  
        print(arquivo.read())

def procurar(hospedeFind):
    index=0
    flag=0
    arquivo = open("Hotel/hotel.txt", "r") 
    for line in arquivo:
        index +=1
        if hospedeFind == eval(line)['Nome']:
            print(line)
            flag = 1
    if flag == 0:
        print("Hospede não encontrado")

def checkout(hospedeFind):
    index=0
    flag=0
    arquivo = open("Hotel/hotel.txt", "r") 
    for line in arquivo:
        index +=1
        if hospedeFind == eval(line)['Nome']:
            chave=index
            flag = 1
    if flag == 0:
        print("Hospede não encontrado")
    else:
        try:
            with open('hotel/hotel.txt', 'r') as fr:
                # reading line by line
                lines = fr.readlines()
                
          
                # pointer for position
                ptr = 1
      
                # opening in writing mode
                with open('hotel/hotel.txt', 'w') as fw:
                    for line in lines:
                
                        # we want to remove 5th line
                        if ptr != chave:
                            fw.write(line)
                        ptr += 1
            print("Deleted")
      
        except:
            print("Oops! someting error")