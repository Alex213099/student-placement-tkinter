from tkinter import*
root=Tk()
root.geometry("400x400")
root.title("Enter your Input Here")
def clicked():
   
    label2=Label(root,text="Hello "+entry1.get())
    label2.pack()

label1=Label(root,text="Enter your name below")
label1.pack()
entry1=Entry(root,width=50)
entry1.insert(0,"Enter your name")
entry1.pack()
button1=Button(root,text="Click me",fg="white",bg="black",command=clicked)
button1.pack()
root.mainloop()