import socket

host = "192.168.0.17"
port = 9090

player_name=input()

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))

server.listen(5)

while True:
    comunication_socket, address=server.accept()
    message=comunication_socket.recv(2048).decode('utf-8')
    print(message)
    myMessage=input()
    comunication_socket.send(player_name," ",myMessage).encode('utf-8')

comunication_socket.close()
