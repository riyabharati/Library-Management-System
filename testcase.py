import unittest
from connection import Library

class Test(unittest.TestCase):
    """The Unit Testing For the  LIBRARY MANAGEMENT SYSTEM IS DONE HERE
        Inherites TestCase from unittest module/library

        methods:
        test_admin_login: returns Ok (asserting true value if the result contains successfully fetched login credentials)
        test_add_user: returns ok  if the user is successfully added
        test_issued_book_list: returns Ok if result contains successfully fetched issued book data


    """

    def test_admin_login(self):
        obj = Library()
        result = obj.admin_login('riya','admin')
        print(result)
        self.assertTrue(result)

    def test_add_user(self):
        obj = Library()
        result = obj.add_user('siya','siya kumari','admin')
        self.assertTrue(result)

    def test_issued_book_list(self):
        obj = Library()
        result = obj.issued_book_list(4)
        self.assertTrue(result)

    def test_add_student(self):
        obj = Library()
        result = obj.add_student('Gangan','9876564787','Kathamandu')
        self.assertTrue(result)

    def test_add_book(self):
        obj = Library()
        result = obj.add_book('Programming Pearls','Jon Louis Bentley', 'YES')
        self.assertTrue(result)

    def test_issue_book(self):
        obj = Library()
        result =  obj.issue_book(4, 4)
        self.assertTrue(result)