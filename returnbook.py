from tkinter import *
from tkinter import messagebox
import os, sys
from datetime import datetime, date
import mysql.connector
from mysql.connector import Error


class ReturnBook(Tk):
    def __init__(self):
        super().__init__()
        self.iconbitmap(r'libico.ico')
        self.title("BOOK RETURN")
        self.maxsize(450, 350)
        self.canvas = Canvas(width=500, height=417, bg='lavender')
        self.canvas.pack()
        self.cal = 0
        a = StringVar()

        def return_book():
            if len(a.get()) == '0':
                messagebox.showerror("Error","Please Enter The Book Id")
            else:
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                                        database='db_library',
                                                        user='root',
                                                        password='', port = 3341)
                    self.mycursor = self.conn.cursor()

                    self.mycursor.execute("Select book_id from issue_book where return_date = '' and book_id = %s",[a.get()])
                    temp = self.mycursor.fetchone()
                    if temp:
                        self.mycursor.execute("update book set availability ='YES' where book_id = %s", [a.get()])
                        self.conn.commit()
                        now = datetime.now()
                        idate = now.strftime('%Y-%m-%d %H:%M:%S')
                        self.mycursor.execute("update issue_book set return_date = %s where book_id = %s", [idate,a.get()])
                        self.conn.commit()
                        self.conn.close()
                        messagebox.showinfo('Info', 'Succesfully Returned')
                        d = messagebox.askyesno("Confirm", "Return more books?")
                        if d:
                            self.destroy()
                            os.system('python returnbook.py')
                        else:
                            self.destroy()
                    else:
                        messagebox.showinfo("Oop's", "Book not yet issued")
                except Error:
                    messagebox.showerror("Error","Something Goes Wrong")


        Label(self, text='RETURN BOOK', fg ='black',bg='thistle', font=('arial', 20, 'bold')).place(x=100, y=20)
        Label(self, text='ENTER ISSUE ID:', bg = 'white', font=('Courier new ', 15)).place(x=20, y=120)
        Entry(self, textvariable=a, width=30).place(x=220, y=124)
        Button(self, text="Return", width=20, command = return_book).place(x=230, y=180)
        Button(self, text  ='Exit', width =20, bg= 'thistle', command = exit).place(x= 290, y=320)

    def exit(self):
        exit()


ReturnBook().mainloop()

