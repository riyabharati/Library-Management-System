from tkinter import *
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
import os
import sys

#creating window
class AddBook(Tk):
    def __init__(self):
        super().__init__()
        self.iconbitmap(r'libico.ico')
        self.maxsize(480,360 )
        self.minsize(480,360)
        self.title('ADD BOOK')
        self.canvas = Canvas(width=500, height=500, bg='lavender')
        self.canvas.pack()
        a = StringVar()
        b = StringVar()
        c = StringVar()
        #verifying Input

        def add_book():
            if len(b.get()) == 0 or len(c.get()) == 0:
                messagebox.showerror("Error","Please Enter The Details")
            else:
                g = 'YES'
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                         database='db_library',
                                         user='root',
                                         password='', port = 3341)
                    self.myCursor = self.conn.cursor()
                    self.myCursor.execute("Insert into book(name,author,availability) values (%s,%s,%s)",[b.get(),c.get(),g])
                    self.conn.commit()
                    messagebox.showinfo('Info', 'Succesfully Added')
                    ask = messagebox.askyesno("Confirm", "Do you want to add another book?")
                    if ask:
                        self.destroy()
                        os.system('python addbook.py')
                    else:
                        self.destroy()
                except Error:
                    messagebox.showerror("Error","Check The Details")


        #creating input box and label
        Label(self, text='').pack()
        Label(self, text='BOOK DETAILS',bg='thistle',fg='black',font=('Courier new', 20, 'bold')).place(x=150, y=70)
        Label(self, text='').pack()
        Label(self, text='BOOK NAME:',bg='white',fg='black', font=('Courier new', 10, 'bold')).place(x=60, y=180)
        Entry(self, textvariable=b, width=30).place(x=170, y=182)
        Label(self, text='BOOK AUTHOR:',bg='white',fg='black', font=('Courier new', 10, 'bold')).place(x=60, y=230)
        Entry(self, textvariable=c, width=30).place(x=170, y=232)
        Button(self, text="Submit", command = add_book, bg = 'thistle').place(x=245, y=300)
        Button(self, text="Exit", command=self.exit).place(x=430, y=300)

    def exit(self):
        exit()

AddBook().mainloop()