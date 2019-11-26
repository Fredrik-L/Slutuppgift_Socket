import socket
from threading import Thread
import pickle
#Import my file that will create and save media objects to file.
import Classes

#Librarian instance, will handle the media.
librarian = Classes.Librarian()
#Client dict, key is the socket and the value is the addres
clients = {}
#login info, key is username and value is password.
user_info = {
    "Fredrik": "1",
    "Erik": "1",
    "Janne": "1"
    }

def create_media(media_type, media_info):
    """
        Creates and saves the media info to file.
        Input is media type and media info. 
    """
    if media_type == "Book":
        librarian.get_Books_From_Client(media_info = media_info)
    if media_type == "Cd":
        librarian.get_CDs_From_Client(media_info = media_info)
    if media_type == "Movie":
        librarian.get_Movies_From_Client(media_info = media_info)
    librarian.save_To_File()

def receive(connection):
    """
        Recives data will split the data into a command and a message.
        The data will look like "cmd//msg".
        Input is a socket.
    """
    while True:
        data = connection.recv(4024)
        if not data:
            del(clients[connection])
            break
        data = data.decode()
        cmd, message = data.split("//", 1)
        address = clients[connection]
        #Row 43 is only when running test, else comment out
        #username = "Test"

        if cmd == "login":
            username, password = message.split(",")
            if user_info.get(username) == password:
                connection.send(b"login//succeed")
            else:
                connection.send(b"login//failed")

        print("Recived Command: " + cmd + ". From ip: " + address[0] + " Username: " + username)

        if cmd == "quit":
        #Will remove the socket from the client list and
        #break from the loop then close down the socket.
            del(clients[connection])
            break
        

        if cmd == "show_Media":
        #Clears the list then read in all the media info from the file.
        #Clearing the list first because i do not want duplicates.
            librarian.book_list.clear()
            librarian.cd_list.clear()
            librarian.movie_list.clear()

            librarian.get_All_Media_From_File()
            librarian.sort_list()
        #Appending all the media info into a list, then sending the list 
        #with help by the module pickle.
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
        #If the cmd is create, the message will be "media_type//media_info"
        #all the clients will recive a message that a user inputed a media.
            media_Type, media_Info = message.split("//", 1) 
            print("Recived media: " + message)
            create_media(media_Type, media_Info)
            broadcast(media_Type, username)
        
    connection.close()
def broadcast(media_type, username):
    """
        broadcasts a message to all the clients.
        Inputs media_type and username.
    """
    message = "broadcast//" + username + " added a new: " + media_type
    for connection in clients:
        connection.send(message.encode())

def Main():
    """
        Main function, 
    """
    host = ""
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host,port))

    print("Socket using port: ", port)
    s.listen(2)

    while True:
        connection, addres = s.accept()
        print("Connectd to : ", addres[1])
        clients[connection] = addres
        
        myThread = Thread(target = receive, args=(connection,))
        myThread.start()

    s.close()

if __name__ == '__main__':   
    Main()
