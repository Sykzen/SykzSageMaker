import time, socket, os
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_number=0

def receive():
    socket.bind(("10.3.141.1", 8080)) # Creation du serveur
    socket.listen(3) # Mise en ecoute d'un client
    BUFFER_SIZE = 4096

    print( " >> Attente d'une nouvelle connexion...")
    conn, adresse = socket.accept() # accepte le client

    print (" >> Vous etes connecte avec : " + adresse[0])
    with open("File_compile.py", "wb") as f:
        while True:
            bytes_read = conn.recv(BUFFER_SIZE)
            if not bytes_read:    
                break
            f.write(bytes_read)
    ipsender=adresse[0]
    conn.close()
    socket.close()
    Compile(ipsender)
def Compile(ipsender):
    print(ipsender)
    import subprocess
    with open("output_N_"+str(client_number)+".txt", "w+") as output:
        subprocess.call(["python", "test.py"], stdout=output)
    
    send("output_N_"+str(client_number)+".txt",ipsender)
# close the server socket
def send(nomFiche,host):
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if nomFich != "":
        try:
            fich = open(nomFich, "rb") # test si le fichier existe
        except:
            print (" >> le fichier '" + nomFich + "' est introuvable.")
            time.sleep(2)
            exit()
        octets = os.path.getsize(nomFich) / 1024
        print (" Envoie du fichier " + nomFich + "' [" + str(octets) + " Ko]")
        try:
            socket.connect((host, 8080)) # test si le serveur existe
        except:
            print ("le serveur '" + host + "' est introuvable.")
            time.sleep(2)
            exit()
        BUFFER_SIZE = 4096
       # socket.send(nomFich.encode())
        #stroctets=str(octets)
        #socket.send(stroctets.encode())
        while True:
            bytes_read = fich.read(BUFFER_SIZE)
            if not bytes_read:
                break
            socket.sendall(bytes_read)


            #octets = octets * 1024 # Reconverti en octets
            #fich = open(nomFich, "rb")
            #num=0
            #if octets > 1024:	# Si le fichier est plus lourd que 1024 on l'envoi par paquet   
            #    for i in range(int(octets / 1024)):                        
             #       fich.seek(num, 0) # on se deplace par rapport au numero de caractere (de 1024 a 1024 octets)
              #      donnees = fich.read(1024) # Lecture du fichier en 1024 octets
               #     socket.sendall(donnees) 
                #    num = num + 1024
            
            #else: # Sinon on envoi tous d'un coup
             #   donnees = fich.read()
              #  socket.send(donnees)
            #fich.close()
        
        fich.close()
        socket.close()
while True:
    receive()











#while (conn.connect):
 #   recu = ""
  #  recu = conn.recv(1024)
   # if not recu : break
    #nomFich = "test.py"                   
    #f = open(nomFich, "wb")      
    #f.write(recu)

    