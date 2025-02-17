from tkinter import *
class Root(Tk):
    def __init__(self):
        super().__init__()
        self.title("Class and Tkinter")
        self.geometry("700x450")

        self.label1=Label(self,text="Hello This is a Label",font=("Helvetica",20))
        self.label1.pack()

        self.button1=Button(self,text="click me",command=self.change)
        self.button1.pack()
        #create a status variable
        self.status=True
        My_frame(self)
    

    def change(self):
        if self.status==True:
            self.label1.config(text="Goodbye world")
            self.status=False
        else :
            self.label1.config(text="Hello world")
            self.status=True
class My_frame(Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.pack()
        self.button1=Button(self,text="something",command=parent.change)
        self.button1.grid(row=0 ,column=0)
        self.button2=Button(self,text="something",command=parent.change)
        self.button2.grid(row=0 ,column=1)
        self.button3=Button(self,text="something",command=parent.change)
        self.button3.grid(row=0 ,column=2)
        
root=Root()
root.mainloop()



        

    
                 
                 
