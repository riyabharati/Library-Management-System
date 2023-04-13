from tkinter import *
from tkinter import messagebox
import os
import sys
from tkinter import ttk
import mysql.connector
from mysql.connector import Error

#creating window
class Dashboard(Tk):
    """ This class is for dashboard design and quickly access the tools for library management system and to show brief
    list of issued book
        Methods:
             add_student(),
             add_student(),
             add_student(),
    """
    def __init__(self):
        super().__init__()
        #self.iconbitmap(r'libico.ico')
        self.configure(bg='blue')
        self.canvas = Canvas(width=1366, height=768, bg='lightskyblue')
        self.canvas.pack()
        self.maxsize(1355, 768)
        self.minsize(1355,768)
        self.state('zoomed')
        self.title('LIBRARY MANAGEMENT SYSTEMS')
        self.a = StringVar()
        self.b = StringVar()
        self.mymenu = Menu(self)

        def add_student():
            ''' This method added the students in the list, interact in the library'''
            os.system('python addstudent.py')
        def add_book():
            os.system('python addbook.py')
        def delete_book():
            os.system('python deletebook.py')
        def delete_student():
            os.system('python deletestudent.py')
        def issue_book():
            os.system('python issuebook.py')
        def return_book():
            os.system('python returnbook.py')
        def search_student():
            os.system('python searchstudent.py')
        def search_book():
            os.system('python searchbook.py')
        def update_student():
            os.system('python updatestudent.py')
        def logout_view():
            confirmation = messagebox.askyesno("Confirm", "Are you sure, you want to Logout? ")
            if confirmation:
                self.destroy()
                os.system('python adminlogin.py')
        def add_user():
            os.system('python adduser.py')
        def delete_user():
            os.system('python deleteuser.py')

        def library_statistics():
            os.system('python librarystatistics.py')




#creating table

        self.listTree = ttk.Treeview(self,height=14,columns=('Student','Book','Issue Date','Return Date'))
        self.vsb = ttk.Scrollbar(self,orient="vertical",command=self.listTree.yview)
        self.hsb = ttk.Scrollbar(self,orient="horizontal",command=self.listTree.xview)
        self.listTree.configure(yscrollcommand=self.vsb.set,xscrollcommand=self.hsb.set)
        self.listTree.heading("#0", text='ID')
        self.listTree.column("#0", width=100,minwidth=50,anchor='center')
        self.listTree.heading("Student", text='Student')
        self.listTree.column("Student", width=200, minwidth=200,anchor='center')
        self.listTree.heading("Book", text='Book')
        self.listTree.column("Book", width=200, minwidth=200,anchor='center')
        self.listTree.heading("Issue Date", text='Issue Date')
        self.listTree.column("Issue Date", width=125, minwidth=125,anchor='center')
        self.listTree.heading("Return Date", text='Return Date')
        self.listTree.column("Return Date", width=125, minwidth=125, anchor='center')
        self.listTree.place(x=320,y=360)
        self.vsb.place(x=1060,y=361,height=300)
        self.hsb.place(x=330,y=650,width=730)
        ttk.Style().configure("Treeview",font=('Times new Roman',15))

        list1 = Menu(self)
        list1.add_command(label = "Add User", command= add_user)
        list1.add_command(label = "Delete User", command= delete_user)

        self.mymenu.add_cascade(label='Admin Tools', menu=list1)
        self.mymenu.add_cascade(label='Library Statistics', command = library_statistics)

        self.config(menu=self.mymenu)

        def find_student():
            if(len(self.studid.get())==0):
                messagebox.showinfo("Error", "Empty Field")
            else:
                try:
                    conn = mysql.connector.connect(host = 'localhost', database = 'db_library', user='root',
                                         password = '',port=3341)
                    cursor = conn.cursor()
                    change = int(self.studid.get())
                    cursor.execute("Select bi.issue_id,s.name,b.name,bi.issue_date,bi.return_date from issue_book bi,"
                                   "student s,book b where s.stud_id = bi.stud_id and b.book_id = bi.book_id "
                                   "and s.stud_id = %s",[change])
                    pc = cursor.fetchall()
                    if pc:
                        self.listTree.delete(*self.listTree.get_children())
                        for row in pc:
                            self.listTree.insert("", 'end', text=row[0], values=(row[1], row[2], row[3], row[4]))
                    else:
                        messagebox.showinfo("Error", "Either ID is wrong or the book is not yet issued on this ID")
                except Error:
                    # print(Error)
                    messagebox.showerror("Error", "Something Goes Wrong")

        def find_book():
            if (len(self.bookid.get()) == 0):
                messagebox.showinfo("Error", "Empty Field!")
            else:
                try:
                    self.conn = mysql.connector.connect(host='localhost',database='db_library',
                                                                user='root', password='', port=3341)
                    self.myCursor = self.conn.cursor()
                    book = int(self.bookid.get())
                    self.myCursor.execute(
                                "Select bi.issue_id,s.name,b.name,bi.issue_date,bi.return_date from issue_book bi,"
                                "student s,book b where s.stud_id = bi.stud_id and b.book_id = bi.book_id "
                                "and b.book_id = %s",[book])
                    self.pc = self.myCursor.fetchall()
                    if self.pc:
                            self.listTree.delete(*self.listTree.get_children())
                            for row in self.pc:
                                    self.listTree.insert("", 'end', text=row[0],
                                                         values=(row[1], row[2], row[3], row[4]))
                    else:
                                messagebox.showinfo("Error", "Either ID is wrong or The book is not yet issued")
                except Error:
                            messagebox.showerror("Error", "Something Goes Wrong")

        def check():
            try:
                conn = mysql.connector.connect(host='localhost',database='db_library',
                                                       user='root', password='', port= 3341)
                mycursor = conn.cursor()
                mycursor.execute("Select * from admin")
                z = mycursor.fetchone()
                if not z:
                    messagebox.showinfo("Error", "Please Register A user")
                    x = messagebox.askyesno("Confirm", "Do you want to register a user")
                    if x:
                        self.destroy()
                        os.system('python adduser.py')
                else:
                    #label and input box
                    self.label3 = Label(self, text='LIBRARY MANAGEMENT SYSTEM',fg='black',bg="deepskyblue" ,font=('Courier new',
                                                                                                                  30, 'bold'))
                    self.label3.place(x=350, y=22)
                    self.label4 = Label(self, text="ENTER STUDENT",bg="deepskyblue", font=('Courier new', 18, 'bold'))
                    self.label4.place(x=130, y=107)
                    self.studid = Entry(self, textvariable=self.a, width=90)
                    self.studid.place(x=405, y=110)
                    self.srt = Button(self, text='Find', width=15, font=('arial', 10), command= find_student).place(x=1000, y=106)
                    self.label5 = Label(self, text="ENTER THE BOOK ID",bg="deepskyblue", font=('Courier new', 18, 'bold'))
                    self.label5.place(x=75, y=150)
                    self.bookid = Entry(self, textvariable=self.b, width=90)
                    self.bookid.place(x=405, y=160)
                    self.brt = Button(self, text='Find', width=15, font=('arial', 10), command = find_book).place(x=1000, y=150)
                    self.label6 = Label(self, text="INFORMATION DETAILS",bg="deepskyblue",  font=('Courier new', 15, 'underline',
                                                                                                  'bold'))
                    self.label6.place(x=560, y=300)
                    self.button = Button(self, text="Add Student", width=15, font=('Courier new', 10),
                                         command=add_student).place(x= 240, y = 200)
                    self.button = Button(self, text='Search Student', width=25, font=('Courier new', 10),
                                         command= search_student).place(x=240,y=250)
                    self.button = Button(self, text='Search Book', width=25, font=('Courier new', 10),
                                         command = search_book).place(x=520,y=250)
                    self.brt = Button(self, text="Issue Book", width=15, font=('Courier new', 10),
                                      command = issue_book).place(x=800, y=250)
                    self.brt = Button(self, text="Add Book", width=15, font=('Courier new', 10),
                                      command = add_book).place(x= 1000 , y = 200)
                    self.brt = Button(self, text="Return Book", width=15, font=('Courier new', 10),
                                      command = return_book).place(x=1000, y=250)
                    self.brt = Button(self, text="LOGOUT", width=15,bg="red", font=('Courier new', 10),
                                      command = logout_view).place(x=1150, y=105)
                    self.button = Button(self, text='Delete Student', width=25, font=('Courier new', 10),
                                         command = delete_student).place(x=100, y=290)
                    self.button = Button(self, text='Update Student', width=25, font=('Courier new', 10),
                                         command = update_student).place(x=320, y=290)
                    self.brt = Button(self, text="Delete Book", width=15, font=('Courier new', 10),
                                      command = delete_book).place(x=800, y=290)

            except Error:
                messagebox.showinfo("Error", "Somethings Goes Wrong")

        check()

        Label(self, text="For More Feature Call : 04378298 Or Visit Our Site www.library.edu", width=200,
                                  bg='black', fg='white').place(x=0, y=660)
        Button(self, text="Exit", width=15, bg='deepskyblue', command=self.exit).place(x=1150, y=630)

    def exit(self):
            exit()

Dashboard().mainloop()
