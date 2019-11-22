import socket
from threading import Thread
import Classes
import pickle

librarian = Classes.Librarian()
clients = {}
user_info = {
    "Fredrik": "Fredrik1",
    "Erik": "Erik1",
    "Janne": "Janne1"
    }

def create_media(media_type, media_info):
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
        cmd, message = data.split("//", 1)
        address = clients[connection]

        if cmd == "login":
            username, password = message.split(",")
            if user_info.get(username) == password:
                connection.send(b"login//succeed")
            else:
                connection.send(b"login//failed")
        if cmd == "quit":
            del(clients[connection])
            break

        if cmd == "show_Media":
            librarian.book_list.clear()
            librarian.cd_list.clear()
            librarian.movie_list.clear()

            librarian.get_All_Media_From_File()

            send_list = []
            if len(librarian.book_list) > 0:
                send_list.append("Books")
                for book in librarian.book_list:
                    book_str = Classes.Book.get_Book_Attribute(book)
                    send_list.append(book_str)

            if len(librarian.cd_list) > 0:
                send_list.append("Cds")
                for cd in librarian.cd_list:
                    cd_str = Classes.Cd.get_Cd_Attribute(cd)
                    send_list.append(cd_str)

            if len(librarian.movie_list) > 0:
                send_list.append("Movies")
                for movie in librarian.movie_list:
                    movie_str = Classes.Movie.get_Movie_Attribute(movie)
                    send_list.append(movie_str)

            connection.send(pickle.dumps(send_list))

        if cmd == "create":
            media_Type, media_Info = message.split("//", 1) 
            print("Recived media: " + message)
            create_media(media_Type, media_Info)
            broadcast(media_Type, username)
        
        print("Recived Command: " + cmd + ". From ip: " + address[0] + " Username: " + username)

    connection.close()
def broadcast(media_type, username):
    message = "broadcast//" + username + " added a new: " + media_type
    for connection in clients:
        connection.send(message.encode())

def Main():
    host = ""
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
    
    s.close()
    
Main()
