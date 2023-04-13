from tkinter import *
from tkinter import messagebox
import os
from tkinter import ttk
import mysql.connector
from mysql.connector import Error
from bubblesorting import Sort


#creating window
class LibraryStatistics(Tk):
    def __init__(self):
        super().__init__()
        #self.iconbitmap(r'libico.ico')
        self.configure(bg='gray')
        self.canvas = Canvas(width=1366, height=768, bg='lightskyblue')
        self.canvas.pack()
        self.maxsize(1360, 700)
        self.minsize(1360,700)
        self.state('zoomed')
        self.title('STATISTICS')
        self.a = StringVar()
        self.b = StringVar()
        self.mymenu = Menu(self)


#creating table
        self.label6 = Label(self, text="ALL STUDENT", bg="deepskyblue", font=('Courier new', 15, 'underline', 'bold'))
        self.label6.place(x=290, y=10)
        self.listTree_stu = ttk.Treeview(self,height=14,columns=('Name', 'Phonenumber','Address'))
        # self.vsb = ttk.Scrollbar(self,orient="vertical",command=self.listTree.yview)
        # self.hsb = ttk.Scrollbar(self,orient="horizontal",command=self.listTree.xview)
        # self.listTree.configure(yscrollcommand=self.vsb.set,xscrollcommand=self.hsb.set)
        self.listTree_stu.heading("#0", text='Student ID')
        self.listTree_stu.column("#0", width=20, minwidth=100, anchor='center')
        self.listTree_stu.heading("Name", text='Name')
        self.listTree_stu.column("Name", width=200, minwidth=140,anchor='center')
        self.listTree_stu.heading("Phonenumber", text='Phonenumber')
        self.listTree_stu.column("Phonenumber", width=200, minwidth=140,anchor='center')
        self.listTree_stu.heading("Address", text='Address')
        self.listTree_stu.column("Address", width=220, minwidth=140, anchor='center')
        self.listTree_stu.place(x=20,y=50)
        # self.vsb.place(x=900,y=361,height=287)
        # self.hsb.place(x=290,y=650,width=700)
        ttk.Style().configure("Treeview",font=('Times new Roman',13))

        def student_list(self):
            try:
                conn = mysql.connector.connect(host='localhost', database='db_library', user='root',
                                               password='', port=3341)
                cursor = conn.cursor()
                cursor.execute("Select * from student")
                pc = cursor.fetchall()
                pc1 =[]
                pc2 = []
                for i,row in enumerate(pc):
                    pc1.append(pc[i][1])
                pc1 = Sort.bubbleSort(pc1)
                for i, value in enumerate(pc1):
                    for j,row in enumerate(pc):
                        if value == pc[j][1]:
                            pc2.append(pc[j])
                if pc:
                    self.listTree_stu.delete(*self.listTree_stu.get_children())
                    for row in pc2:
                        self.listTree_stu.insert("", 'end', text=row[0], values=(row[1], row[2], row[3]))

            except Error:
                # print(Error)
                messagebox.showerror("Error", "Something Goes Wrong")
        student_list(self)


        self.label7 = Label(self, text="ALL BOOKS", bg="deepskyblue", font=('Courier new', 15, 'underline', 'bold'))
        self.label7.place(x=1000, y=10)
        self.listTree_book = ttk.Treeview(self, height=14, columns=('Name', 'Author', 'Availability'))
        # self.vsb = ttk.Scrollbar(self, orient="vertical", command=self.listTree.yview)
        # self.hsb = ttk.Scrollbar(self, orient="horizontal", command=self.listTree.xview)
        # self.listTree.configure(yscrollcommand=self.vsb.set, xscrollcommand=self.hsb.set)
        self.listTree_book.heading("#0", text='Book_ID')
        self.listTree_book.column("#0", width=50, minwidth=130, anchor='center')
        self.listTree_book.heading("Name", text='Name')
        self.listTree_book.column("Name", width=200, minwidth=140, anchor='center')
        self.listTree_book.heading("Author", text='Author')
        self.listTree_book.column("Author", width=200, minwidth=140, anchor='center')
        self.listTree_book.heading("Availability", text='Availability')
        self.listTree_book.column("Availability", width=200, minwidth=120, anchor='center')
        self.listTree_book.place(x=700, y=50)
        # self.vsb.place(x=1028, y=361, height=287)
        # self.hsb.place(x=320, y=650, width=700)
        ttk.Style().configure("Treeview", font=('Times new Roman', 13))

        def book_list(self):
            try:
                conn = mysql.connector.connect(host='localhost', database='db_library', user='root',
                                               password='', port=3341)
                cursor = conn.cursor()
                cursor.execute("Select * from book")
                pc = cursor.fetchall()
                pc1 = []
                pc2 = []
                for i, row in enumerate(pc):
                    pc1.append(pc[i][1])
                pc1 = Sort.bubbleSort(pc1)
                for i, value in enumerate(pc1):
                    for j, row in enumerate(pc):
                        if value == pc[j][1]:
                            pc2.append(pc[j])
                if pc:
                    self.listTree_book.delete(*self.listTree_book.get_children())
                    for row in pc2:
                        self.listTree_book.insert("", 'end', text=row[0], values=(row[1], row[2], row[3]))

            except Error:
                # print(Error)
                messagebox.showerror("Error", "Something Goes Wrong")
        book_list(self)

        self.label8 = Label(self, text="ISSUED BOOK", bg="deepskyblue", font=('Courier new', 15, 'underline', 'bold'))
        self.label8.place(x=620, y=365)
        self.listTree = ttk.Treeview(self, height=12, columns=('BookID', 'StudentID', 'Issued Date', 'Return Date'))
        # self.vsb = ttk.Scrollbar(self, orient="vertical", command=self.listTree.yview)
        # self.hsb = ttk.Scrollbar(self, orient="horizontal", command=self.listTree.xview)
        # self.listTree.configure(yscrollcommand=self.vsb.set, xscrollcommand=self.hsb.set)
        self.listTree.heading("#0", text='IssuedID')
        self.listTree.column("#0", width=20, minwidth=140, anchor='center')
        self.listTree.heading("BookID", text='BookID')
        self.listTree.column("BookID", width=200, minwidth=140, anchor='center')
        self.listTree.heading("StudentID", text='StudentID')
        self.listTree.column("StudentID", width=200, minwidth=140, anchor='center')
        self.listTree.heading("Issued Date", text='Issued Date')
        self.listTree.column("Issued Date", width=230, minwidth=130, anchor='center')
        self.listTree.heading("Return Date", text='Return Date')
        self.listTree.column("Return Date", width=260, minwidth=170, anchor='center')
        self.listTree.place(x=225, y=398)
        # self.vsb.place(x=1028, y=361, height=287)
        # self.hsb.place(x=320, y=650, width=700)
        ttk.Style().configure("Treeview", font=('Times new Roman', 13))

        def issued_list(self):
            try:
                conn = mysql.connector.connect(host='localhost', database='db_library', user='root',
                                               password='', port=3341)
                cursor = conn.cursor()
                cursor.execute("Select * from issue_book order by book_id")
                pc = cursor.fetchall()
                if pc:
                    self.listTree.delete(*self.listTree.get_children())
                    for row in pc:
                        self.listTree.insert("", 'end', text=row[0], values=(row[1], row[2], row[3], row[4]))

            except Error:
                # print(Error)
                messagebox.showerror("Error", "Something Goes Wrong")

        issued_list(self)

        Button(self, text = 'Exit', width= 20, bg = 'deepskyblue', command = exit).place(x=1200, y =650)

    def exit(self):
            exit()

LibraryStatistics().mainloop()
