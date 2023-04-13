from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error


class SearchBook(Tk):
    def __init__(self):
        super().__init__()
        f = StringVar()
        g = StringVar()
        self.title("SEARCH BOOK")
        self.maxsize(800,500)
        self.minsize(800,500)
        self.canvas = Canvas(width=800, height=500, bg='lavender')
        self.canvas.pack()
        self.iconbitmap(r'libico.ico')
        l1=Label(self,text="SEARCH LIBRARY",bg='thistle', font=("Courier new",20,'bold')).place(x=290,y=20)
        l = Label(self, text="SEARCH BY:",bg='WHITE', font=("Courier new", 15, 'bold')).place(x=60, y=96)

        def insert(data):
            self.listTree.delete(*self.listTree.get_children())
            for row in data:
                self.listTree.insert("", 'end', text=row[0], values=(row[1], row[2], row[3]))

        def getter_setter():
            if (len(g.get())) == 0:
                messagebox.showinfo('Error', 'First select a item')
            elif (len(f.get())) == 0:
                messagebox.showinfo('Error', 'Enter the ' + g.get())
            elif g.get() == 'Book Name':
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                                        database='db_library',
                                                        user='root',
                                                        password='', port =3341)
                    self.mycursor = self.conn.cursor()
                    self.mycursor.execute("Select * from book where name LIKE %s", ['%' + f.get() + '%'])
                    self.pc = self.mycursor.fetchall()
                    if self.pc:
                        insert(self.pc)
                    else:
                        messagebox.showinfo("Oop's", "Either Book Name is incorrect or it is not available")
                except Error:
                    messagebox.showerror("Error", "Something goes wrong")
            elif g.get() == 'Author Name':
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                                        database='db_library',
                                                        user='root',
                                                        password='', port = 3341)
                    self.mycursor = self.conn.cursor()
                    self.mycursor.execute("Select * from book where author LIKE %s", ['%' + f.get() + '%'])
                    self.pc = self.mycursor.fetchall()
                    if self.pc:
                        insert(self.pc)
                    else:
                        messagebox.showinfo("Oop's", "Author Name not found")
                except Error:
                    messagebox.showerror("Error", "Something goes wrong")
            elif g.get() == 'Book Id':
                try:
                    self.conn = mysql.connector.connect(host='localhost',
                                                        database='db_library',
                                                        user='root',
                                                        password='', port = 3341)
                    self.mycursor = self.conn.cursor()
                    self.mycursor.execute("Select * from book where book_id = %s", [f.get()])
                    self.pc = self.mycursor.fetchall()
                    if self.pc:
                        insert(self.pc)
                    else:
                        messagebox.showinfo("Oop's", "Either Book Id is incorrect or it is not available")
                except Error:
                    messagebox.showerror("Error", "Something goes wrong")


        b=Button(self,text="Find",width=15,bg='thistle',font=("Courier new",10,'bold'),command = getter_setter).place(x=495,y=148)
        c=ttk.Combobox(self,textvariable=g,values=["Book Name","Author Name","Book Id"],width=40,
                       state="readonly").place(x = 200, y = 100)
        en = Entry(self,textvariable=f,width=43).place(x=200,y=155)
        la = Label(self, text="ENTER:",bg='white', font=("Courier new", 15, 'bold')).place(x=100, y=150)

        def handle(event):
            if self.listTree.identify_region(event.x,event.y) == "separator":
                return "break"


        self.listTree = ttk.Treeview(self, height=13,columns=('Book Name', 'Book Author', 'Availability'))
        self.vsb = ttk.Scrollbar(self,orient="vertical",command=self.listTree.yview)
        self.listTree.configure(yscrollcommand=self.vsb.set)
        self.listTree.heading("#0", text='Book ID', anchor='center')
        self.listTree.column("#0", width=120, anchor='center')
        self.listTree.heading("Book Name", text='Book Name')
        self.listTree.column("Book Name", width=200, anchor='center')
        self.listTree.heading("Book Author", text='Book Author')
        self.listTree.column("Book Author", width=200, anchor='center')
        self.listTree.heading("Availability", text='Availability')
        self.listTree.column("Availability", width=200, anchor='center')
        self.listTree.bind('<Button-1>', handle)
        self.listTree.place(x=20, y=200)
        self.vsb.place(x=735,y=200,height=287)
        ttk.Style().configure("Treeview", font=('Times new Roman', 13))

        Button(self, text='Exit', bg= 'thistle', command = exit).place(x= 755, y=450)

    def exit(self):
        exit()

SearchBook().mainloop()