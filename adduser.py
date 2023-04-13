from tkinter import *
from tkinter import messagebox
import re
from tkinter import ttk
import mysql.connector
from mysql.connector import Error
import os, sys


# creating window
class AddUser(Tk):
    def __init__(self):
        super().__init__()
        self.iconbitmap(r'libico.ico')
        self.maxsize(500, 417)
        self.minsize(500, 417)
        self.title('ADD USER')
        self.canvas = Canvas(width=500, height=417, bg='lavender')
        self.canvas.pack()
        # creating variables Please chech carefully
        u = StringVar()
        n = StringVar()
        p = StringVar()

        def insert():
            try:
                self.conn = mysql.connector.connect(host='localhost',
                                                    database='db_library',
                                                    user='root',
                                                    password='',port= 3341)
                self.myCursor = self.conn.cursor()
                self.myCursor.execute(
                    "Insert into admin(user,name,password) values (%s,%s,%s)", [u.get(), n.get(), p.get()])
                self.conn.commit()
                messagebox.showinfo("Done", "User Inserted Successfully")
                ask = messagebox.askyesno("Confirm", "Do you want to add another user?")
                if ask:
                    self.destroy()
                    os.system('python adduser.py')
                else:
                    self.destroy()
                    self.myCursor.close()
                    self.conn.close()
            except Error:
                messagebox.showinfo("Error", "Something Goes Wrong")

        # label and input
        Label(self, text='USER DETAILS', bg='thistle', fg='black', font=('Courier new', 25, 'bold')).place(x=130, y=22)
        Label(self, text='USERNAME:', bg='WHITE', font=('Courier new', 10, 'bold')).place(x=70, y=82)
        Entry(self, textvariable=u, width=30).place(x=200, y=84)
        Label(self, text='NAME:', bg='WHITE', font=('Courier new', 10, 'bold')).place(x=70, y=130)
        Entry(self, textvariable=n, width=30).place(x=200, y=132)
        Label(self, text='PASSWORD:', bg='WHITE', font=('Courier new', 10, 'bold')).place(x=70, y=180)
        Entry(self, textvariable=p, width=30).place(x=200, y=182)
        Button(self, text="Submit", bg = 'thistle',width=15, command=insert).place(x=230, y=220)
        Button(self, text="Exit", width=15, command=self.exit).place(x=230, y=360)

    def exit(self):
        exit()
AddUser().mainloop()