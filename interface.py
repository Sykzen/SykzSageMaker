import tkinter as tk
from tkinter import *
import tkinter.filedialog
import PIL
from PIL import ImageTk
from PIL import Image

#Fonction AskopenFilename pour ouvrir un dossier courant
LST_Types = [( "Script python" , ".py" )]
def askopenfile():
        return tk.filedialog.askopenfilename ( title = "Sélectionnez un fichier ..." , filetypes = LST_Types )

#Interface Graphique
root = tk.Tk()
root.title("SykzSageMaker")
canvas1 = tk.Canvas(root, width = 1000, height = 600, bg = 'lightsteelblue2', relief = 'raised')
canvas1.pack()
#canvas1.grid()


button1=tk.Button(text='Déposer votre Fichier' , command=askopenfile)
canvas1.create_window(500,50,window=button1)
canvas1.pack()

imageLogo  = Image.open("static/logo.png")
imageLogo  =imageLogo.resize((100,130),Image.ANTIALIAS)
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
Srv1=Server("Raspbery#0001","192.178.145.0","Disponible",(220,200))
Srv1.setStatus()
#
Srv2=Server("Raspbery#0002","192.198.195.147","Disponible",(220,400))
Srv2.setStatus()
#
Srv3=Server("Raspbery#0003","192.138.125.50","Disponible",(720,200))
Srv3.setStatus()
#
Srv4=Server("Raspbery#0004","192.144.125.44","Occupé",(720,400))
Srv4.setStatus()






#tk.Label(frm,text='Browse').grid(column=2, row=9)
#tk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=10)
root.mainloop()

def sendSSH(i):
    pass
