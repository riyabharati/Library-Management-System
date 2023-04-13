from tkinter import *
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error

# creating widow
class UpdateStudent(Tk):
    def __init__(self):
        super().__init__()
        self.iconbitmap(r'libico.ico')
        self.maxsize(650, 400)
        self.minsize(650, 400)
        self.title("UPDATE STUDENT")
        self.canvas = Canvas(width=1366, height=768, bg='lavender')
        self.canvas.pack()
        a = StringVar()
        b = StringVar()
        c = StringVar()
        d = StringVar()

        def insert(data):
            b.set('')
            c.set('')
            d.set('')
            for row in data:
                b.set(row[1])
                c.set(row[2])
                d.set(row[3])

        def fetch_student():
            try:
                self.conn = mysql.connector.connect(host='localhost',
                                                    database='db_library',
                                                    user='root',
                                                    password='', port=3341)
                self.mycursor = self.conn.cursor()
                self.mycursor.execute("Select * from student where stud_id = %s", [a.get()])
                self.pc = self.mycursor.fetchall()
                if self.pc:
                    insert(self.pc)
                else:
                    messagebox.showinfo("Oop's", "Either ID is incorrect or it is not available")
            except Error:
                messagebox.showerror("Error", "Something goes wrong")

        def update_student():
            name = b.get()
            phone_number = c.get()
            address = d.get()
            try:
                self.conn = mysql.connector.connect(host='localhost',
                                                    database='db_library',
                                                    user='root',
                                                    password='', port=3341)
                self.mycursor = self.conn.cursor()
                self.mycursor.execute("update student set name = %s, phone_number = %s, address = %s where stud_id = %s",
                                      [name,phone_number,address,a.get()])
                self.conn.commit()
                self.conn.close()
                messagebox.showinfo('Info', 'Succesfully Updated')
            except Error:
                messagebox.showerror("Error", "Something goes wrong")

        Label(self, text="ENTER STUDENT ID:", bg='WHITE', fg='black', font=('Courier new', 15, 'bold')).place(x=5, y=44)
        Entry(self, textvariable=a, width=30).place(x=400, y=44)
        Button(self, text='Enter', width=15, font=('arial', 10), command = fetch_student).place(x=400, y=90)
        Label(self, text="Update INFORMATION", bg='thistle', fg='black', font=('Courier new', 15, 'bold')).place(x=200, y =140)
        Label(self, text="ENTER STUDENT NAME:", bg='WHITE', fg='black', font=('Courier new', 15, 'bold')).place(x=70, y=190)
        Entry(self, textvariable=b, width=30).place(x=430, y=190)
        Label(self, text="ENTER STUDENT PHONE NUMBER:", bg='WHITE', fg='black', font=('Courier new', 15, 'bold')).place(x=70, y=240)
        Entry(self, textvariable=c, width=30).place(x=430, y=240)
        Label(self, text="ENTER STUDENT ADDRESS:", bg='WHITE', fg='black', font=('Courier new', 15, 'bold')).place(x=70, y=290)
        Entry(self, textvariable=d, width=30).place(x=430, y=290)
        Button(self, text='Update', width=15, font=('arial', 10), command = update_student).place(x=430, y=320)
        Button(self, text='Exit', width = 15, bg = 'thistle', command = exit).place(x= 0, y = 370)

    def exit(self):
        exit()

UpdateStudent().mainloop()
