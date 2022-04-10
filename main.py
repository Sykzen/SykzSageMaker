import time, socket, os
import logging
liste_of_addr_ip=["10.3.141.216","10.3.141.158","10.3.141.88"]
def receive():
    """Fonction pour écouter la demande d'un client"""
    socketa = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Connection socket
    socketa.bind(("10.3.141.1", 8080)) # Creation du serveur
    socketa.listen(3) # Mise en ecoute d'un client
    conn, adresse = socketa.accept() # accepte le client
    free_srv=Fetch_Free_srv(adresse[0]): #return la recherche d'une adresse ip d'unserveur valide
    socketa.connect((adresse[0], 8080))
    mysocket.send(free_srv)
    socketa.close()
def Fetch_Free_srv(addr:str) -> str:
    socketa.close()
    socketa = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    for i in liste_of_addr_ip:
        if is_socket_closed(socketa,i): #si on trouve un serveur on retourn l'addr ip au client
            return i
        else:
            pass
        
        
        



def is_socket_closed(socketa: socket.socket,ip) -> bool:
    """Fonction pour verifier si le socket socketa arrive à se connecter au serveur IP
        donc verifier qu'il est disponible
        socket,ip -> bool
    """
    try:
        socketa.connect((ip, 8080))
        return True
    except:
        return False
    
while True:
    receive()
    
    
    
    
    
    
    
