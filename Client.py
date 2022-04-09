import time, socket, os
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print (" --------------------------------------------------------------------")
print (" # AWS SageMaker Cluster ")
print (" #  Créez, entraînez et déployez rapidement et facilement des modèles de machine learning (ML)  ")
print (" # pour tous les cas d'utilisation avec une infrastructure, des outils et des flux entièrement gérés")
print (" -----------------------------------------------------------------")

def SendFile(host,nomFich):
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

        while True:
            bytes_read = fich.read(BUFFER_SIZE)
            if not bytes_read:
                break
            socket.sendall(bytes_read)
        

        fich.close()
        socket.send(socket.getsockname()[0].encode())
        socket.close()
    else:
        print("fichier vide")
SendFile("10.3.141.1","test.py")