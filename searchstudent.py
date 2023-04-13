from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import os, glob
import mysql.connector
from mysql.connector import Error


class SearchStudent(Tk):
    def __init__(self):
        super().__init__()
        f = StringVar()
        g = StringVar()
        self.title("SEEARCH STUDENT")
        self.maxsize(800, 520)
        self.canvas = Canvas(width=1366, height=768, bg='lavender')
        self.canvas.pack()
        self.iconbitmap(r'libico.ico')
        l1 = Label(self, text="SEARCH STUDENT", bg='thistle', font=("Courier new", 20, 'bold')).place(x=290, y=40)
        l = Label(self, text="SEARCH BY:", bg='white', font=("Courier new", 15, 'bold')).place(x=180, y=100)

        def insert(data):
            self.listTree.delete(*self.listTree.get_children())
            for row in data:
                self.listTree.insert("", "end", text=row[0], values=(row[1], row[2], row[3]))
        def getter_setter():
            if (len(self.entry.get())) == 0:
                messagebox.showinfo('Error', 'First select a item')
            elif (len(self.combo.get())) == 0:
                messagebox.showinfo('Error', 'Enter the '+self.combo.get())
            elif self.combo.get() == 'Name':
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                         database='db_library',
                                         user='root',
                                         password='',port= 3341)
                    self.mycursor = self.conn.cursor()
                    name = self.entry.get()
                    self.mycursor.execute("Select * from student where name like %s",['%'+name+'%'])
                    pc = self.mycursor.fetchall()
                    if pc:
                        insert(pc)
                    else:
                        messagebox.showinfo("Oop's","Name not found")
                except Error:
                    messagebox.showerror("Error", "Something goes wrong")
            elif self.combo.get() == 'ID':
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                         database='db_library',
                                         user='root',
                                         password='', port = 3341)
                    self.mycursor = self.conn.cursor()
                    id = self.entry.get()
                    self.mycursor.execute("Select * from student where stud_id = %s", [id])
                    pc = self.mycursor.fetchall()
                    if pc:
                        insert(pc)
                    else:
                        messagebox.showinfo("Oop's", "Id not found")
                except Error:
                    messagebox.showerror("Error", "Something goes wrong")

        self.b = Button(self, text="Find", width=8, bg = 'thistle', font=("Courier new", 8, 'bold'), command= getter_setter)
        self.b.place(x=400, y=170)
        self.combo = ttk.Combobox(self, textvariable=g, values=["Name", "ID"], width=40, state="readonly")
        self.combo.place(x=330, y=105)
        self.entry = Entry(self, textvariable=f, width=43)
        self.entry.place(x=330, y=145)
        self.la = Label(self, text="ENTER:", bg='white', font=("Courier new", 15, 'bold')).place(x=180, y=140)
        self.listTree = ttk.Treeview(self, height=13, columns=('Student Name', 'Phone Number', 'Address'))
        self.vsb = ttk.Scrollbar(self, orient="vertical", command=self.listTree.yview)
        self.listTree.configure(yscrollcommand=self.vsb.set)
        self.listTree.heading("#0", text='Student ID', anchor='w')
        self.listTree.column("#0", width=100, anchor='w')
        self.listTree.heading("Student Name", text='Student Name')
        self.listTree.column("Student Name", width=200, anchor='center')
        self.listTree.heading("Phone Number", text='Phone Number')
        self.listTree.column("Phone Number", width=200, anchor='center')
        self.listTree.heading("Address", text='Address')
        self.listTree.column("Address", width=200, anchor='center')
        self.listTree.place(x=20, y=200)
        self.vsb.place(x=720, y=200, height=287)
        ttk.Style().configure("Treeview", font=('Times new Roman', 15))

        Button(self, text='Exit', bg = 'thistle', command = exit).place(x= 750, y= 463)

    def exit(self):
        exit()
SearchStudent().mainloop()

