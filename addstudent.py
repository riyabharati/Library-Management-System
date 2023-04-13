from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os
import mysql.connector
from mysql.connector import Error


#creating window
class AddStudent(Tk):
    def __init__(self):
        super().__init__()
        self.iconbitmap(r'libico.ico')
        self.maxsize(500,417)
        self.minsize(500,417)
        self.title('Add STUDENT')
        self.canvas = Canvas(width=500, height=417, bg='lavender')
        self.canvas.pack()
        n = StringVar()
        p = StringVar()
        a = StringVar()

        def add_student():
            if len(n.get()) < 1:
                messagebox.showinfo("Oop's", "Please Enter Your Name")
            elif len(p.get()) < 1:
                messagebox.showinfo("Oop's","Please Enter Your Phone Number")
            elif len(a.get()) < 1:
                messagebox.showinfo("Oop's", "Please Enter Your Address")
            else:
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                                        database='db_library',
                                                        user='root',
                                                        password='', port= 3341)
                    self.myCursor = self.conn.cursor()
                    name1 = n.get()
                    pn1 = p.get()
                    add1 = a.get()
                    self.myCursor.execute("Insert into student(name,phone_number,address) values (%s,%s,%s)",[name1,pn1,add1])
                    self.conn.commit()
                    messagebox.showinfo("Done","Student Inserted Successfully")
                    ask = messagebox.askyesno("Confirm","Do you want to add another student?")
                    if ask:
                     self.destroy()
                     os.system('python addstudent.py')
                    else:
                     self.destroy()
                     self.myCursor.close()
                     self.conn.close()
                except Error:
                    messagebox.showerror("Error","Something goes wrong")


        # label and input box
        Label(self, text='STUDENT DETAILS',bg='lavender', font=('Courier new', 25, 'bold')).place(x=90,y= 30)
        Label(self, text='NAME:',bg='lavender', font=('Courier new', 10, 'bold')).place(x=70, y=82)
        Entry(self, textvariable=n, width=30).place(x=200, y=84)
        Label(self, text='PHONE NUMBER:',bg='lavender', font=('Courier new', 10, 'bold')).place(x=70, y=130)
        Entry(self, textvariable=p, width=30).place(x=200, y=132)
        Label(self, text='ADDRESS:',bg='lavender', font=('Courier new', 10, 'bold')).place(x=70, y=180)
        Entry(self, textvariable=a, width=30).place(x=200, y=182)
        Button(self, text="Submit",width = 15, bg = 'thistle',command = add_student).place(x=230, y=220)
        Button(self, text="Exit", width=15,  bg='thistle', command=self.exit).place(x=230, y=380)
    def exit(self):
        exit()
AddStudent().mainloop()
