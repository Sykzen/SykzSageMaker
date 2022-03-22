import tkinter as tk



root = tk.Tk()
frm = tk.Frame(root)
frm.grid(column=50, row=50)
tk.Label(frm, text="Hello World!").grid(column=0, row=0)
tk.columnconfigure(50, 20)
tk.Button(frm,text='Browse' ).grid(column=2, row=0)
tk.Label(frm,text='Browse').grid(column=2, row=1)
tk.Label(frm,text='Browse' ).grid(column=2, row=2)
tk.Label(frm,text='Browse' ).grid(column=2, row=3)
tk.Label(frm,text='Browse' ).grid(column=2, row=4)
tk.Label(frm,text='Browse' ).grid(column=2, row=5)
tk.Label(frm,text='Browse' ).grid(column=2, row=6)
tk.Label(frm,text='Browse' ).grid(column=2, row=7)
tk.Label(frm,text='Browse').grid(column=2, row=8)
tk.Label(frm,text='Browse').grid(column=2, row=9)
tk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=10)
root.mainloop()


LST_Types = [( "Script python" , ".py" )]
def askopenfile():
        return askopenfilename ( title = "Sélectionnez un fichier ..." , filetypes = LST_Types )




