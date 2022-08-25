from tkinter import *
from tkinter.filedialog import askopenfilename
from speed import NeedForSpeed

def openfile():

   filename = askopenfilename(parent=root)
   f = open(filename)
   f.read()

root = Tk()
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=openfile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)


root.config(menu=menubar)
root.mainloop()