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
canvas1.grid()
imageLogo  = Image.open("static/logo.png")
imageLogo  =imageLogo.resize((150,150),Image.ANTIALIAS)
imageLogo  =ImageTk.PhotoImage(imageLogo)
canvas1.create_image(0,1, anchor = tk.NW, image=imageLogo)
root.mainloop()



#♥tk.Button(frm,text='Déposer votre Fichier' , command=askopenfile).grid(column=2, row=0)

#tk.Label(frm,text='Browse').grid(column=2, row=9)
#tk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=10)


def sendSSH(i):
    pass
