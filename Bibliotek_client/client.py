import socket
from appJar import gui
from threading import Thread
import pickle
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Functions for creating medias
def create_Book():
    entryValue = get_Entries()
    send_media("Book", entryValue)
def create_Cd():
    entryValue = get_Entries()
    send_media("Cd", entryValue)
def create_Movie():
    entryValue = get_Entries()
    send_media("Movie",entryValue)
def send_media(media_Type, media_Info):
    """Send the media to the server. Inputs are media type and the media info.
        It will send a string ex "Book/title,writer,pages,price,year".
        Then clear all the entries.  
    """
    send_Str = "create//" + media_Type + "//"
    for words in media_Info:
        send_Str += str(words + ",")
    send_Str = send_Str.rstrip(",")
    app.infoBox("Sent","Du har skickat :" + send_Str)
    s.send(send_Str.encode())
    app.clearAllEntries()

def get_Entries():
    """Gets all the Entries and returns the values as a list. 
    """
    return_values = []
    allEntries = app.getAllEntries()
    entriesValue = list(allEntries.values())
    for value in entriesValue:
        if value != "":
            return_values.append(value)
    return return_values

def close():
    """
        Close down the client. Sends a message to the server,
        and then waits for the threads and closes down.
    """
    s.send(b"quit//")
    myThread.join()
    s.close()
    app.stop()

def click(btn):
    """Buttons Book, Cd, Movie

        Switches between Frames where you add media object.
    """
    if btn == "Book": app.selectFrame("Media", 0)
    if btn == "Cd": app.selectFrame("Media", 1)
    if btn == "Movie": app.selectFrame("Media",2)

def show_media():
    s.send(b"show_Media//")
    app.clearListBox("Media Objects")
    
def listen_server(server):
    """
        Listen after data, the data will be made of "cmd//message".
        Depending on the cmd if will do diffrent things.
    """
    while True:
        data = server.recv(4024)
        try:
            data = data.decode()
            cmd, message = data.split("//", 1)
            if cmd == "login":
                if message == "succeed":
                    app.hideSubWindow("Login")
                    app.showSubWindow("client_App")

                if message == "failed":
                    app.infoBox("Error", "Wrong user info.")

            if cmd == "broadcast":
                app.addListItem("msg", message)
            
        except ValueError:
            pass

        if not data:
            print("hejdå")
            server.close()
            break
        try:
            recv_str = pickle.loads(data)
            app.addListItems("Media Objects", recv_str)
        except TypeError:
            pass

def start_Conn(host,port):
    """
        Will connecnt to the host and port.
        Then create a thread.
    """
    s.connect((host,port))
    myThread = Thread(target = listen_server, args=(s,))
    myThread.start()
    return myThread
def press(btn):
    """
        Login buttons.
    """
    if btn == "Exit":
        close()
    if btn == "Login":
        username = app.getEntry("Username")
        password = app.getEntry("Password")
        if username == "" or password == "":
            app.infoBox("Error", "You need to enter username and password.")
        else:
            message = "login//" + username + "," + password
            s.send(message.encode())
            app.clearAllEntries()



app = gui("Bibliotek", "600x700")

app.startSubWindow("Login")
app.addLabel("Login for Fish Library!")
app.setSticky("NESW")
app.addLabelEntry("Username")
app.addLabelSecretEntry("Password")
app.addButtons(["Login", "Exit"], press)
app.stopSubWindow()

app.startSubWindow("client_App")
app.setSticky("NESW")

app.startFrameStack("Media")

app.startFrame("Book_Frame")
app.setSticky("WE")
app.addLabel("Adding a Book")
app.addLabel("Title of Book")
app.addEntry("title_book")
app.addLabel("Writer")
app.addEntry("writer")
app.addLabel("Pages of the books")
app.addEntry("pages")
app.addLabel("Purchased price of Book")
app.addEntry("purchased_Price_Book")
app.addLabel("Purchase year")
app.addEntry("purchased_Year_Book")
app.addButton("Send Book", create_Book)

app.stopFrame()

app.startFrame("Cd_Frame")
app.setSticky("WE")
app.addLabel("Adding a Cd")
app.addLabel("Title of Cd")
app.addEntry("title_Cd")
app.addLabel("Artist")
app.addEntry("artist")
app.addLabel("Amount of songs")
app.addEntry("amount_Songs")
app.addLabel("Cd length in min")
app.addEntry("length_Cd")
app.addLabel("Purchased price of Cd")
app.addEntry("purchased_Price_Cd")
app.addButton("Send Cd", create_Cd)
app.stopFrame()

app.startFrame("Movie_Frame")
app.setSticky("WE")
app.addLabel("Adding a Movie")
app.addLabel("Title of Movie")
app.addEntry("title_Movie")
app.addLabel("Director")
app.addEntry("director")
app.addLabel("Movie length in min")
app.addEntry("length_Movie")
app.addLabel("Purchased price of Movie")
app.addEntry("purchased_Price_Movie")
app.addLabel("Purchase Year")
app.addEntry("purchased_Year_Movie")
app.addLabel("Damage of Movie(1-10)")
app.addEntry("dmg_movie")
app.addButton("Send Moive", create_Movie)
app.stopFrame()
app.stopFrameStack()

app.startFrame("menu_frame", column = 1 , row = 0)

app.addButton("Book", click)
app.addButton("Cd", click)
app.addButton("Movie", click)
app.addButton("Show all media", show_media)
app.addButton("Close", close)

app.stopFrame()

app.startFrame("listbox_frame",colspan=2)
app.addListBox("Media Objects")
app.stopFrame()

app.startFrame("msg_frame",column=2, row = 0, rowspan=2)
app.addListBox("msg")
app.stopFrame()

myThread = start_Conn("127.0.0.1", 12345)
app.stopSubWindow()

app.go(startWindow = "Login")