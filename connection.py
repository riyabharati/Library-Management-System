import mysql.connector  # Importing library that helps connecting to the MYSQL
from datetime import date, datetime

class Connection:

    def __init__(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='db_library',
            port = 3341
        )
        self.cursor = self.conn.cursor()


class Library(Connection):
    def __init__(self):
        super(Library, self).__init__()

    def admin_login(self, user, password):
        self.cursor.execute('select * from admin where user = %s and password = %s', (user, password))
        data = self.cursor.fetchone()
        self.conn.close()
        return data

    def add_user(self, user, name, password):
        self.cursor.execute('Insert into admin(user,name,password) values (%s,%s,%s)', [user, name, password])
        self.conn.commit()
        return True

    def issued_book_list(self, stud_id):
        self.cursor.execute("Select bi.issue_id,s.name,b.name,bi.issue_date,bi.return_date from issue_book bi,"
                                   "student s,book b where s.stud_id = bi.stud_id and b.book_id = bi.book_id "
                                   "and s.stud_id = %s", [stud_id])
        data = self.cursor.fetchall()
        self.conn.close()
        return data

    def add_student(self,name,phone_number,address):
        self.cursor.execute('Insert into student(name,phone_number,address) values (%s,%s,%s)', [name,phone_number,address])
        self.conn.commit()
        return True

    def add_book(self,name,author,availability='YES'):
        self.cursor.execute('Insert into book(name,author,availability) values (%s,%s,%s)', [name,author,availability])
        self.conn.commit()
        return True

    def issue_book(self, book_id, stud_id):
        self.cursor.execute("Select availability from book where availability = 'YES' and book_id = %s", [book_id])
        self.pc = self.cursor.fetchall()
        if self.pc:
            now = datetime.now()
            idate = now.strftime('%Y-%m-%d %H:%M:%S')
            self.cursor.execute(
                "Insert into issue_book(book_id,stud_id,issue_date,return_date) values (%s,%s,%s,%s)",
                [book_id, stud_id, idate, ''])
            self.conn.commit()
            self.cursor.execute("Update book set availability = 'NO' where book_id = %s", [book_id])
            self.conn.commit()
        else:
            book_id = str(book_id)
            print("Oop's", "Book id " + book_id + " is not available")
        self.conn.close()
        return True
    