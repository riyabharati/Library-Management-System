from tkinter import *
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error

# creating widow
class DeleteBook(Tk):
    def __init__(self):
        super().__init__()
        self.iconbitmap(r'libico.ico')
        self.maxsize(450, 250)
        self.minsize(450, 250)
        self.title("DELETE BOOK")
        self.canvas = Canvas(width=1366, height=768, bg='lavender')
        self.canvas.pack()
        a = StringVar()

        def delete_book():
            if len(a.get()) == 0:
                messagebox.showinfo("Error", "Please Enter A Valid Book Id")
            else:
                d = messagebox.askyesno("Confirm", "Are you sure you want to remove the Book?")
                if d:
                    try:
                        self.conn = mysql.connector.connect(host='localhost',
                                                            database='db_library',
                                                            user='root',
                                                            password='', port = 3341)
                        self.myCursor = self.conn.cursor()
                        self.myCursor.execute("Delete from book where book_id = %s", [a.get()])
                        self.conn.commit()
                        self.myCursor.close()
                        self.conn.close()
                        messagebox.showinfo("Confirm", "Book Removed Successfully")
                        a.set("")
                    except Error:
                        messagebox.showerror("Error", "Something goes wrong")

        Label(self, text="ENTER BOOK ID:", bg='thistle', fg='black', font=('Courier new', 15, 'bold')).place(x=5, y=40)
        Entry(self, textvariable=a, width=30).place(x=210, y=44)
        Button(self, text='Delete', width=15, font=('arial', 10), command = delete_book).place(x=210, y=90)
        Button(self, text="Exit", width=15, bg = 'thistle',command=self.exit).place(x=330, y=220)

    def exit(self):
            exit()

DeleteBook().mainloop()
