from tkinter import *
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error

# creating widow
class DeleteUser(Tk):
    def __init__(self):
        super().__init__()
        self.iconbitmap(r'libico.ico')
        self.maxsize(400, 200)
        self.minsize(400, 200)
        self.title("DELETE USER")
        self.canvas = Canvas(width=1366, height=768, bg='lavender')
        self.canvas.pack()
        a = StringVar()

        def delete_user():
            if len(a.get()) ==0:
                messagebox.showinfo("Error","Please Enter A Valid Id")
            else:
                d = messagebox.askyesno("Confirm", "Are you sure you want to remove the user?")
                if d:
                    try:
                        self.conn = mysql.connector.connect(host='localhost',
                                         database='db_library',
                                         user='root',
                                         password='', port = 3341)
                        self.myCursor = self.conn.cursor()
                        self.myCursor.execute("Delete from admin where id = %s",[a.get()])
                        self.conn.commit()
                        self.myCursor.close()
                        self.conn.close()
                        messagebox.showinfo("Confirm","User Removed Successfully")
                        a.set("")
                    except:
                        messagebox.showerror("Error","Something goes wrong")

        Label(self, text="ENTER USER ID:", bg='thistle', fg='black', font=('Courier new', 15, 'bold')).place(x=5, y=40)
        Entry(self, textvariable=a, width=30).place(x=190, y=44)
        Button(self, text='Remove', width=15, font=('arial', 10),command = delete_user).place(x=200, y=90)
        Button(self, text = 'Exit', width = 13, bg= 'thistle', font=('arial', 10), command = exit).place(x=270, y=165)

    def exit(self):
        exit()

DeleteUser().mainloop()
