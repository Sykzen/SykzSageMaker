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
            fich.close()

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
        while (socket.connect):
            octets = octets * 1024 # Reconverti en octets
            fich = open(nomFich, "rb")
            num=0
            if octets > 1024:	# Si le fichier est plus lourd que 1024 on l'envoi par paquet   
                for i in range(int(octets / 1024)):                        
                    fich.seek(num, 0) # on se deplace par rapport au numero de caractere (de 1024 a 1024 octets)
                    donnees = fich.read(1024) # Lecture du fichier en 1024 octets
                    socket.sendall(donnees) 
                    num = num + 1024
            
            else: # Sinon on envoi tous d'un coup
                donnees = fich.read()
                socket.send(donnees)
            fich.close()
    else:
        print("fichier vide")
