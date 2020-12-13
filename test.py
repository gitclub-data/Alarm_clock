from tkinter import *
import tkinter.filedialog as fd
root = Tk()

def browsefunc():
    filename = fd.askopenfilename()
    pathlabel.config(text=filename)

browsebutton = Button(root, text="Browse", command=browsefunc)
browsebutton.pack()

pathlabel = Label(root)
pathlabel.pack()

root.mainloop()