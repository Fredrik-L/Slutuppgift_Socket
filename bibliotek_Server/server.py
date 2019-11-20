import socket
from threading import Thread
import Classes
import pickle
librarian = Classes.Librarian()
clients = {}

def create_media(media_type, media_info):
    media_type = media_type.strip("/")
    if media_type == "Book":
        librarian.get_Books_From_Client(media_info = media_info)
        librarian.save_To_File()
    if media_type == "Cd":
        librarian.get_CDs_From_Client(media_info = media_info)
        librarian.save_To_File()
    if media_type == "Movie":
        librarian.get_Movies_From_Client(media_info = media_info)
        librarian.save_To_File()

def receive(connection):
    while True:
        data = connection.recv(1024)
        data = data.decode()
        if data == "quit":
            del(clients[connection])
            break
        if data == "Show_Media/":
            librarian.get_All_Media_From_File()
            book_list = []
            for book in librarian.book_list:
                book_str = Classes.Book.get_Book_Attribute(book)
                book_list.append(book_str)

            book_send_List = pickle.dumps(book_list)
            connection.send(book_send_List)
            """for book in librarian.book_list:
                book_str = Classes.Book.get_Book_Attribute(book)
                connection.send(b"Book/" + book_str.encode())

            for cd in librarian.cd_list:
                cd_str = Classes.Cd.get_Cd_Attribute(cd)
                connection.send(b"Cd/" + cd_str.encode())

            for movie in librarian.movie_list:
                movie_str = Classes.Movie.get_Movie_Attribute(movie)
                connection.send(b"Movie/" + movie_str.encode())
                """
        media_type, media_info = data.split("/",1)
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
        return s
    
s = Main()
