import socket
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
    while True:
        media_info = connection.recv(1024)
        media_info = media_info.decode()
        media_type, media_info = media_info.split("/",1)
        print("Type of Media :", media_type)
        print("Recived :", media_info)
        create_media(media_type, media_info)
    connection.close()


def Main():
    host = "127.0.0.1"
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host,port))

    print("Socket using port: ", port)
    s.listen(2)

    while True:
        connection, addres = s.accept()
        print("Connectd to : ", addres[0])
        clients[connection] = addres
        myThread = Thread(target = receive, args=(connection,))
        myThread.start()

Main()