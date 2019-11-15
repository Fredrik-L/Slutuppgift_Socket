import socket
from appJar import gui
from threading import Thread

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def create_book():
    x = app.getAllEntries()
    y = list(x.values())
    sentence = "Book/"
    for words in y:
        sentence += str(words + ",")

    sentence = sentence.rstrip(",")
    app.infoBox("hej", sentence)
    s.send(sentence.encode())

def listen_server(server):
    while True:
        data = server.recv(1024)
        if not data:
            break
        if data == b"quit":
            break
def start_Conn(host,port):

    s.connect((host,port))
    myThread = Thread(target = listen_server, args=(s,))
    myThread.start()

app = gui("Bibliotek", "400x400")

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
app.addButton("Add Book", create_book)

start_Conn("127.0.0.1", 12345)

app.go()