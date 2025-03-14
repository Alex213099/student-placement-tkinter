from tkinter import *
import tkinter as tk
from tkinter import messagebox 
import mysql.connector
def connect_db():
    try:
        conn=mysql.connector.connect(
            host="localhost",
            user="root",
            password="alex",
            database="pos_management",
            port='3310'
        
        )
        return conn
    except mysql.connector.Error as err:
        messagebox.showerror(err)
        return None

def fetch_data():
    conn=connect_db()
    if conn==None:
        return []
    
    try:
        with conn.cursor() as cursor:
            cursor.execute("select * from product")
            products=cursor.fetchall()
            for product in products:
                products_listbox.insert("end",f"{product[1]} - KSH{product[2]}  stock {product[5]}")

        return products
    except mysql.connector.Error as err:
        messagebox.showerror(err)
    finally:
        conn.close()

root=Tk()
root.title("Tkinter App")
root.geometry("500x700")
frame1=Frame(root)
frame1.grid(row=0,column=0)
name=Label(frame1,text="name").grid(row=0,column=0)
name_entry=Entry(frame1)
name_entry.grid(row=0,column=1)

email=Label(frame1,text="email").grid(row=1,column=0)
email_entry=Entry(frame1)
email_entry.grid(row=1,column=1)


password=Label(frame1,text="Password")
password.grid(row=2,column=0)
password_entry=Entry(frame1)
password_entry.grid(row=2,column=1)

submit=Button(frame1,text="submit").grid(row=1,column=3)

products_frame=Frame(root)
products_frame.grid(row=0,column=1)

products_listbox=tk.Listbox(products_frame,width=50)
products_listbox.grid(row=0,column=0)


if __name__=="__main__":
    products=fetch_data()
    print(products)





root.mainloop()

            
