import time, socket, os
socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_number=0

def receive():
    socket1.bind(("10.3.141.1", 8080)) # Creation du serveur
    socket1.listen(3) # Mise en ecoute d'un client
    BUFFER_SIZE = 4096

    print( " >> Attente d'une nouvelle connexion...")
    conn, adresse = socket1.accept() # accepte le client

    print (" >> Vous etes connecte avec : " + adresse[0])
    with open("File_compile.py", "wb") as f:
        while True:
            bytes_read = conn.recv(BUFFER_SIZE)
            if not bytes_read:    
                break
            f.write(bytes_read)
    ipsender=adresse[0]
    conn.close()
    socket1.close()
    Compile(ipsender)
def Compile(ipsender):
    print(ipsender)
    import subprocess
    with open("output_N_"+str(client_number)+".txt", "w+") as output:
        subprocess.call(["python", "test.py"], stdout=output)
    
    send("output_N_"+str(client_number)+".txt",ipsender)
# close the server socket
def send(nomFiche,host):
    socket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
            socket2.connect((host, 8080)) # test si le serveur existe
        except:
            print ("le serveur '" + host + "' est introuvable.")
            time.sleep(2)
            exit()
        BUFFER_SIZE = 4096

        while True:
            bytes_read = fich.read(BUFFER_SIZE)
            if not bytes_read:
                break
            socket2.sendall(bytes_read)

        fich.close()
        socket2.close()
while True:
    receive()

    