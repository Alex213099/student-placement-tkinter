from tkinter import *

class App(Tk):
    def __init__(self,title,geometry):
        super().__init__()
        self.title(title)
        self.geometry(f"{geometry[0]}x{geometry[1]}")
        self.label1=Label(self,text="Hello this is a label",font=("helvetica",20))
        self.label1.pack()
        self.menu=Menu(self)
        self.mainloop()

class Menu(Frame):
    def __init__(self,parent):
        super().__init__(parent)
        label3=Label(self,bg="red")
        label3.pack(expand=True,fill=BOTH)
        self.pack()
App("Simple Program",(700,450))