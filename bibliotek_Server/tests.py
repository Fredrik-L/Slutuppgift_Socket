import unittest
import socket
import pickle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 12345))

class test_server(unittest.TestCase):
    
    """def test_listen_server(self):
        data = "login//succeed"
        x = test_client.listen_server(data)
        print(type(x))
        self.assertEqual("succeed", x)
    """
    def test_send(self):
        s.send(b"login//Fredrik,Fredrik1")
        data_login = s.recv(1024)
        data_login = data_login.decode()
        self.assertEqual("login//succeed",data_login)

        s.send(b"login//Fredrik,hej")
        data_login = s.recv(1024)
        data_login = data_login.decode()
        self.assertEqual("login//failed",data_login)
        

    def test_broadcast(self):
        s.send(b"create//book//Bamse,Astrid,200,500,2018")
        data = s.recv(1024)
        data = data.decode()
        right_str = "broadcast//Fredrik added a new: book"
        self.assertEqual(right_str,data)
        


    
unittest.main()
