AF_INET = 1
SOCK_STREAM = 2
host = "127.0.0.1"
port = 12345
class socket():
    def __init__(self,ip,port):
        print("Running Init Method")
    
    def bind(self, socket):
        print("Running Bind Method")

    def listen(self, length):
        print("Running Listen Method")
    def recv(self,data_length):
        print("Running Recv Method")
    def accept(self):
        print("Running Accept Method")
        return self, (host,port)

    def connect(self,addr):
        print("Running Connect Method")
    
    def close(self):
        print("Running Close Method")