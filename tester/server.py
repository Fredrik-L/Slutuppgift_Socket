import socket_test
from threading import Thread
import Classes
librarian = Classes.Librarian()
clients = {}

def create_media(media_type, media_info):
    media_type = media_type.strip("/")
    if media_type == "Book":
        librarian.get_Books_From_Client(media_info = media_info)
        librarian.save_To_File()

def receive(connection):
    media_info = connection.recv(1024)
    #media_info = media_info.decode()
    #media_type, media_info = media_info.split("/",1)
    #print("Type of Media :", media_type)
    media_type = "book"
    print("Recived :", media_info)
    create_media(media_type, media_info)
    connection.close()

def Main():
    host = "127.0.0.1"
    port = 12345
    s = socket_test.socket(socket_test.AF_INET, socket_test.SOCK_STREAM)
    s.bind((host,port))

    print("Socket using port: ", port)
    s.listen(2)
    connection, addres = s.accept()
    print("Connectd to : ", addres[0])
    clients[connection] = addres
    myThread = Thread(target = receive, args=(connection,))
    myThread.start()


Main()