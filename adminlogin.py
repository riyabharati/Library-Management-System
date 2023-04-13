from tkinter import *
from tkinter import messagebox
import mysql.connector
import sys
from mysql.connector import Error
import os


class Library(Tk):
    """ This class is for adminlogin  to manage and use of the system """

    def __init__(self):
        super().__init__()
        self.a = StringVar()
        self.b = StringVar()
        self.maxsize(1300,650)
        self.minsize(1300,650)
        self.configure(bg="lightskyblue")
        self.title("LOGIN PAGE FOR LIBRARY MANAGEMENT SYSTEM")

        def login_view():
            if len(self.user_text.get()) < 0:
                messagebox.showinfo("Username is missing")
            elif len(self.pass_text.get()) < 0:
                messagebox.showinfo("Password is missing")

            else:
                try:
                    conn = mysql.connector.connect(host = 'localhost', database = 'db_library', user='root',password = '',port=3341)
                    cursor = conn.cursor()
                    user = self.user_text.get()
                    password = self.pass_text.get()
                    cursor.execute('select * from admin where user = %s and password = %s', (user,password))
                    pc = cursor.fetchone()
                    if pc:
                        self.destroy()
                        os.system('python dashboardlibrary.py')
                    else:
                        print(pc)
                        messagebox.showinfo('Error', 'Username or password did not match!!')
                        self.user_text.delete(0,END)
                        self.pass_text.delete(0,END)
                except Error:
                    messagebox.showinfo('Error', 'Something went wrong! Try Restarting or check your connection')

        def check():
            self.label = Label(self,text = ' ADMIN LOGIN', bg = 'lightskyblue', fg = 'black', font =  ("courier-new", 24, 'bold'))
            self.label.place(x=500, y=90)
            self.label1 = Label(self, text = 'USER ID:', bg= 'white', fg= 'black', font = ("courier-new", 18, 'bold'))
            self.label1.place(x=370,y=180)
            self.user_text = Entry(self,textvariable=self.a,width = 45)
            self.user_text.place(x=500,y=190)
            self.label2 = Label(self,text = "PASSWORD:", bg = 'white',fg = "black", font = ("courier-new",18,"bold"))
            self.label2.place(x = 340,y=250)
            self.pass_text = Entry(self, show= '*',textvariable =self.b,width= 45)
            self.pass_text.place(x=500,y=255)
            self.btn = Button(self,text= "LOGIN", bg = "bisque", font = 10, width =8,command = login_view).place(x=450,y=300)
            self.label3 = Label(self,text= "Welcome To Library Management System",bg = "bisque", fg = "black",font =
                                                                          ("courier-new",24,"bold")).place(x=350,y=30)
            self.btn = Button(self, text="Exit", bg="bisque", font=10, width=8, command=self.exit).place(x=700, y=300)
            lbl_forgot = Label(self, text="Forgot Password?", fg='blue')
            lbl_forgot.place(x=580, y=500)
            lbl_forgot.bind('<Button-1>', lambda e: self.forgot())
        check()
    def exit(self):
        exit()

    def forgot(self):
        messagebox.showinfo("Forgot Password", "Dont't Worry.\nEnter your Gmail or Phone Number "
                                               "to  to \nrecover your password.")
Library().mainloop()

