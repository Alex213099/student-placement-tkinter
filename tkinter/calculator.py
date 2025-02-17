from tkinter import *

root=Tk()
root.geometry("500x500")
root.title("Calculator")

entry=Entry(root,width=35)
entry.grid(row=0,column=0,columnspan=3,padx=30,pady=10)
def add_values():
    number1=nine.get()
    number2=eight.get()
    result=number1+number2
    entry(text=result)
    

nine=Button(root,text="9",bg="gray",fg="blue",padx=10,pady=10)
nine.grid(row=1,column=0)
eight=Button(root,text="8",padx=10,pady=10)
eight.grid(row=1,column=1)
seven=Button(root,text="7",padx=10,pady=10)
seven.grid(row=1,column=2)
six=Button(root,text="6",padx=10,pady=10)
six.grid(row=2,column=0)
five=Button(root,text="5",padx=10,pady=10)
five.grid(row=2,column=1)
four=Button(root,text="4",padx=10,pady=10)
four.grid(row=2,column=2)
three=Button(root,text="3",padx=10,pady=10)
three.grid(row=3,column=0)
two=Button(root,text="2",padx=10,pady=10)
two.grid(row=3,column=1)
one=Button(root,text="1",padx=10,pady=10)
one.grid(row=3,column=2)
zero=Button(root,text="0",padx=10,pady=10)
zero.grid(row=4,column=0)

add=Button(root,text="+",padx=10,pady=10 ,command=add_values) 
add.grid(row=4,column=1,padx=10,pady=10)
subtract=Button(root,text="-",padx=10,pady=10)
subtract.grid(row=4,column=2,padx=10,pady=10)


root.mainloop()
