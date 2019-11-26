import unittest
import socket
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 12345))

class test_server(unittest.TestCase):
    
    def x_test_recive(self):
        """
            Only works when its the only tests that sends something.
            Tests recive func when a clients are logging in. 
        """
        s.send(b"login//Fredrik,1")
        data_login = s.recv(1024)
        data_login = data_login.decode()
        self.assertEqual("login//succeed",data_login)

        s.send(b"login//Fredrik,hej")
        data_login = s.recv(1024)
        data_login = data_login.decode()
        self.assertEqual("login//failed",data_login)
        

    def test_broadcast(self):
        """
            Needs to have Row 43 in server.py to be able to run.'
            Tests broadcast function, server recives book. Sends back
            a broadcast.
        """
        s.send(b"create//book//Bamse,Astrid,200,500,2018")
        data = s.recv(1024)
        data = data.decode()
        right_str = "broadcast//Test added a new: book"
        self.assertEqual(right_str,data)

    def test_create_media(self):
        """
            Tests that the right information will be writen
            into the right file when a book is created.
        """
        s.send(b"create//Book//Aaaaaa,Astrid,200,500,2015")
        book_list = []
        file_name = os.path.dirname(__file__) + "/Books.txt"

        with open(file_name, "r") as f:
            for book in f:
                book = book.strip("\n")
                book_list.append(book)
        
        self.assertEqual("Aaaaaa,Astrid,500,200,2015,131.2",book_list[0])

    
unittest.main()
