"""
Description: THis is a tkinter program using oop to place students based on performance
author:Alex Kamau
last Date: modified:16/02/2025
Github:Alex21309
"""
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#class definition.
class App(Tk):
    def __init__(self):
        super().__init__()
        #main window structure
        self.geometry("700x450")
        self.title("Student PLacement App")
        

        #defining the labels
        self.name=Label(self,text="Name")
        self.name.grid(row=0,column=0)
        self.marks=Label(self,text="Marks")
        self.marks.grid(row=1,column=0)
        self.gender=Label(self,text="Gender:")
        self.gender.grid(row=2,column=0)
        self.age=Label(self,text="age")
        self.age.grid(row=3,column=0)
        self.disability=Label(self,text="Disability")
        self.disability.grid(row=4,column=0)

        #defining the entry field
        self.entry_name=Entry(self)
        self.entry_name.grid(row=0,column=2)
        self.entry_marks=Entry(self)
        self.entry_marks.grid(row=1,column=2)
        self.entry_gender=Entry(self)
        self.entry_gender.grid(row=2,column=2)
        self.entry_age=Entry(self)
        self.entry_age.grid(row=3,column=2)
        options=["none",'Physical','Mental']
        self.entry_disability=ttk.Combobox(self,values=options)
        self.entry_disability.current(0)
        self.entry_disability.grid(row=4,column=2)
        

        self.submit_btn=Button(self,text='submit', command=self.submit)
        self.submit_btn.grid(row=6,column=2)
    def apply(self):
        gotten=self.ent.get()
        gotten=int(gotten)
        if gotten==1:
            messagebox.showinfo('notification','You have succesfully been placed in a vocational Training')
        elif gotten==2:
            messagebox.showinfo('notification','You have successfully applied to repeat your exam')
        else:
            messagebox.showinfo('notification','Invalid input')
    #method to get and validate the inputed data.
    def submit(self):
        #having a get request to get the values
        try:
            name=self.entry_name.get()
            age=int(self.entry_age.get())
            disability=self.entry_disability.get().lower()
            marks=int(self.entry_marks.get())
            gender=self.entry_gender.get().strip().lower()
            #data validations starts here.
        except Exception as err:
            messagebox.showinfo('validate your entry again')
    

        self.mymessage =Label(self,text=(''))
        self.mymessage.grid(row=9 ,column=6)

        if age <12 or age>18:
            messagebox.showinfo('notification',"Age should only be between 12 and 18")
            self.mymessage.config(text="Age should only be between 12 and 18")
        elif disability=='physical'or disability=='mental':
            if marks >= 250 :
                if gender=='male':
                    messagebox.showinfo('notification','You are placed in a male school fro the special kids')
                    self.mymessage.config(text="You are placed in a male school fro the special kids")

                else:
                    messagebox.showinfo('notification','You are placed in a female school for the specials kids')
                    self.mymessage.config(text="You are placed in a female school for the specials kids")
                    

            else:
                self.mymessage.config(text="You do not meet the minimum requirement of 250 marks .Enter 1 for vocational Training 2. For exam repeatation")
                messagebox.showinfo('notification','You are do not reach the pass mark of 250 .1.Enter to apply for vocational training 2. To apply for exam repeat ')


        else:

            if marks >=400 and marks <= 500:
                messagebox.showinfo('notification','You are placed in a national School')
                self.mymessage.config(text=f"You are placed in a national School for {gender}")
            elif marks >=350 and marks<=399:
                self.mymessage.config(text=f"You are placed in an extra county School for {gender}")

            elif marks >=250 and marks <=349:
                messagebox.showinfo('notification','You are placed in a county School')
                self.mymessage.config(text=f"You are placed in a county School for {gender}")

            else:
                messagebox.showinfo('notification','You do not reach the minimum of 250 marks . Your can either repeat the exam or join a vocational Instituition')
                self.mymessage.config(text="You do not reach the minimum of 250 marks . Your can either repeat the exam or join a vocational Instituition")
                self.ap=Button(self,text='apply',command=self.apply)
                self.ap.grid(row=9,column=1)
                self.ent=Entry(self)
                self.ent.grid(row=9,column=0)

            
#creating an instance of App
app=App()
app.mainloop()
