from datetime import date, datetime
from tkinter import *
from tkinter import messagebox
import os
import sys
import mysql.connector
from mysql.connector import Error

# creating window
class IssueBook(Tk):
    def __init__(self):
        super().__init__()
        self.iconbitmap(r'libico.ico')
        self.title('LIBRARY ADMISINTRATION')
        self.maxsize(440, 300)

        self.canvas = Canvas(width=1366, height=768, bg='lavender')
        self.canvas.pack()
        c = StringVar()
        d = StringVar()

        def issue_book():
            if (len(c.get())) == 0:
                messagebox.showinfo('Error', 'Empty field!')
            elif (len(d.get())) == 0:
                messagebox.showinfo('Error', 'Empty field!')
            else:
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                                        database='db_library',
                                                        user='root',
                                                        password='', port = 3341)
                    self.mycursor = self.conn.cursor()
                    self.mycursor.execute("Select availability from book where availability = 'YES' and book_id = %s",
                                          [c.get()])
                    self.pc = self.mycursor.fetchall()
                    try:
                        if self.pc:
                            print("success")
                            book = c.get()
                            stud = d.get()
                            now = datetime.now()
                            idate = now.strftime('%Y-%m-%d %H:%M:%S')
                            self.mycursor.execute(
                                "Insert into issue_book(book_id,stud_id,issue_date,return_date) values (%s,%s,%s,%s)",
                                [book, stud, idate, ''])
                            self.conn.commit()
                            self.mycursor.execute("Update book set availability = 'NO' where book_id = %s", [book])
                            self.conn.commit()
                            messagebox.showinfo("Success", "Successfully Issue!")
                            ask = messagebox.askyesno("Confirm", "Do you want to add another?")
                            if ask:
                                self.destroy()
                                os.system('python issuebook.py')
                            else:
                                self.destroy()
                        else:
                            messagebox.showinfo("Oop's", "Book id " + c.get() + " is not available")
                    except Error:
                        messagebox.showerror("Error", "Check The Details")
                except Error:
                    messagebox.showerror("Error", "Something goes wrong")


        # label and input box
        Label(self, text='BOOK ISSUING', bg='thistle', font=('Courier new', 24)).place(x=135, y=40)
        Label(self, text='BOOK ID:', bg='white', font=('Courier new', 15), fg='black').place(x=55, y=100)
        Entry(self, textvariable=c, width=40).place(x=170, y=106)
        Label(self, text='STUDENT ID:', bg='white', font=('Courier new ', 15), fg='black').place(x=20, y=150)
        Entry(self, textvariable=d, width=40).place(x=170, y=158)
        Button(self, text="Issue", width=20,command = issue_book).place(x=200, y=200)
        Button(self, text = 'Exit', width = 15,bg ='thistle', command = exit).place(x=315, y=268)

    def exit(self):
        exit()

IssueBook().mainloop()
