import tkinter as tk
from tkinter import *
import tkinter.filedialog
import PIL
from PIL import ImageTk
from PIL import Image
import os
import socket
import time
import shutil
print (" --------------------------------------------------------------------")
print (" # AWS SageMaker Cluster ")
print (" #  Créez, entraînez et déployez rapidement et facilement des modèles de machine learning (ML)  ")
print (" # pour tous les cas d'utilisation avec une infrastructure, des outils et des flux entièrement gérés")
print (" -----------------------------------------------------------------")
#Fonction AskopenFilename pour ouvrir un dossier courant
LST_Types = [( "Script python" , ".py" )]
def Send(host,nomFich):
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
            mysocket.connect(('10.3.141.1', 8080)) # test si le serveur existe
        except:
            print ("le serveur '" + host + "' est introuvable.")
            time.sleep(2)
            exit()
        BUFFER_SIZE = 4096

        while True:
            bytes_read = fich.read(BUFFER_SIZE)
            if not bytes_read:
                break
            mysocket.sendall(bytes_read)

        fich.close()
        global myIp
        myIp=mysocket.getsockname()[0].encode()
        mysocket.close()
    else:
        print("fichier vide")
def Receive():
    socket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket2.bind((myIp, 8080)) # Creation du serveur
    socket2.listen(3) # Mise en ecoute d'un client
    BUFFER_SIZE = 4096

    print( " >> Attente d'une nouvelle connexion...")
    conn, adresse = socket2.accept() # accepte le client
    namefilah=file.split("/")[-1][:-2]
    print (" >> Vous etes connecte avec : " + adresse[0])
    with open("Compiled_"+str(namefilah)+"txt", "wb") as f:
        while True:
            bytes_read = conn.recv(BUFFER_SIZE)
            print(bytes_read)
            if not bytes_read:    
                break
            f.write(bytes_read)
    conn.close()
    socket2.close()
    f.close()
def Make():
    root.destroy()
    Send(host,file)
    print("Fichier Reçu par le serveur Main ")
    print("Recherche des Serveur Disponible ...")
    print("Fichier transferer vers le Host "+str(host))
    print("Fichier Compiler et prêt à être retranferer ")
    print("Fichier Transferer ")
    print("Fichier Entrain de se compiler ")
    Receive()
    print("fichier reçu")
    


def askopenfile():
        global host
        global file
        p=tk.filedialog.askopenfilename ( title = "Sélectionnez un fichier ..." , filetypes = LST_Types )
        file=p
        host="10.3.141.1"
            
#Interface Graphique
root = tk.Tk()
root.title("AmazonSageMaker")
canvas1 = tk.Canvas(root, width = 1000, height = 600, bg = 'lightsteelblue2', relief = 'raised')
canvas1.pack()
#canvas1.grid()


button1=tk.Button(text='Déposer votre Fichier' , command=askopenfile)
canvas1.create_window(500,50,window=button1)
canvas1.pack()
button2=tk.Button(text='Compiler' , command=Make)
canvas1.create_window(450,500,window=button2)
canvas1.pack()

imageLogo  = Image.open("static/logo.png")
imageLogo  =imageLogo.resize((200,130),Image.ANTIALIAS)
imageLogo  =ImageTk.PhotoImage(imageLogo)
canvas1.create_image(0,1, anchor = tk.NW, image=imageLogo)
canvas1.pack()

frames = [PhotoImage(file='static/on.gif',format = 'gif -index %i' %(i)) for i in range(2)]
frames2 = [PhotoImage(file='static/offe.gif',format = 'gif -index %i' %(i)) for i in range(2)]
class Server:
    def __init__(self,ide,ip,status,position):
        self.ide=ide
        self.ip=ip
        self.status=status
        self.position=position
    def setStatus(self):
        ide = tk.Label(root, text="ID :"+self.ide,bg = 'lightsteelblue2')
        ip=  tk.Label(root, text="IP :"+self.ip,bg = 'lightsteelblue2')
        status=tk.Label(root, text="STATUS :"+self.status,bg = 'lightsteelblue2')
        canvas1.create_window(self.position[0]+20, self.position[1], window=ide)
        canvas1.create_window(self.position[0]+20, self.position[1]+50, window=ip)
        canvas1.create_window(self.position[0]+20, self.position[1]+100, window=status)
def setStatusServerX(ide):
    return ide
def update(ind):

    frame = frames[ind]
    frame2 = frames2[ind]
    ind += 1
    ind=ind%2
    label.configure(image=frame,width="120")
    label2.configure(image=frame,width="120")
    label3.configure(image=frame,width="120")
    label4.configure(image=frame2,width="120")
    #canvas1.configure(image=frame)
    root.after(250, update, ind)
label = Label(root,width="120")
label2 = Label(root,width="120")
label3 = Label(root,width="120")
label4 = Label(root,width="120")
canvas1.create_window(100,250,window=label)
canvas1.create_window(100,450,window=label2)
canvas1.create_window(600,250,window=label3)
canvas1.create_window(600,450,window=label4)
#label.pack()
canvas1.pack()
root.after(0, update, 0)
#Server 1
Srv1=Server("Raspbery#0001","10.3.141.14","Disponible",(220,200))
Srv1.setStatus()
#
Srv2=Server("Raspbery#0002","10.3.141.88","Disponible",(220,400))
Srv2.setStatus()
#
Srv3=Server("Raspbery#0003","10.3.141.14","Disponible",(720,200))
Srv3.setStatus()
#
Srv4=Server("Raspbery#0004","10.3.141.44","Occupé",(720,400))
Srv4.setStatus()
root.mainloop()



