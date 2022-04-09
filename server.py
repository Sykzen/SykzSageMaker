import time, socket, os
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
##################################################################
# CREATION DU SERVEUR
##################################################################

print (" >> Creation du serveur (le pare feu peut alerter)")
socket.bind(("10.3.141.1", 8080)) # Creation du serveur
socket.listen(1) # Mise en ecoute d'un client
    
print( " >> Attente d'une nouvelle connexion...")
conn, adresse = socket.accept() # accepte le client

print (" >> Vous etes connecte avec : " + adresse[0])

while (conn.connect):
    recu = ""
    recu = conn.recv(1024)
    if not recu : break
    nomFich = "test.py"                   
    f = open(nomFich, "wb")
    identifier = "oui"        
    f.write(recu)

    