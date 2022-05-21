import socket

host = "192.168.0.17"
port = 9090

player_name=input()

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))

while True:
    print(socket.recv(2048).decode('utf-8'))
    myMessage=input()
    socket.send(player_name," ",myMessage).encode('utf-8')


comunication_socket.close()