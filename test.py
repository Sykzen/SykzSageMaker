
'''---------------Import libraries-------------------'''
import tkinter as tk

'''--------------global variables----------------'''
framelist = []      # List to hold all the frames
frame_index = 0 
count = 0
anim = None
list_gif_frames =[]

'''-----------------methods---------------------'''
     


'''-------------Tkinter GUI main window----------------------'''
window = tk.Toplevel()
window.title("GIF LOADED")
window.geometry("800x800")
'''--------------count all frames in gif and saved in a list-----------------'''
while True:
    try:
        # Read a frame from GIF file
        part = 'gif -index {}'.format(frame_index)
        frame = tk.PhotoImage(file='static/on.gif', format=part)
        print(part)
    except:
        print("break")
        last_frame = frame_index - 1    # Save index for last frame
        break               # Will break when GIF index is reached
    framelist.append(frame)
    print(len(framelist))
    frame_index += 1 
'''------------label to show gif--------------------'''
l1 = tk.Label(window, bg='#202020', image = "")
l1.pack()
'''-----------------button to start gif--------------------'''
def animate_gif(count):  
    global anim
    l1.config(image = framelist[count])
    count +=1
        
    if count > last_frame:
        count = 0  
    #recall animate_gif method    
    anim = window.after(100, lambda :animate_gif(count))   
animate_gif(0)

window.mainloop()
