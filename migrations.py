import os
import paramiko
import pathlib

def SendSSH(ip):
    os.system("ssh pi@" +str(ip))

import tkinter as tk
from tkinter import *
import tkinter.filedialog
import PIL
from PIL import ImageTk
from PIL import Image
import os
import shutil

#Fonction AskopenFilename pour ouvrir un dossier courant
LST_Types = [( "Script python" , ".py" )]
def askopenfile():
        p=tk.filedialog.askopenfilename ( title = "Sélectionnez un fichier ..." , filetypes = LST_Types )
        dest=(os.path.abspath(os.getcwd())+"\\Input").replace("\\","/")
        shutil.move(p,dest)
        return p
#Interface Graphique
root = tk.Tk()

