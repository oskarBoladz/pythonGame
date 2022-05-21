import socket,sys
server="192.168.0.17"
port=5555

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((server,port))
s.listen(2)
def client(self):
    pass
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

print(local_ip)

