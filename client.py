# Python program to implement client side of chat room.
import socket
import select
import sys

FORMAT = "utf-8"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP_address = socket.gethostbyname(socket.gethostname())
Port = 5053
server.connect((IP_address, Port))

usr_name = ''
ip = ''

while True:

    # maintains a list of possible input streams
    sockets_list = [sys.stdin, server]

    read_sockets, write_socket, error_socket = select.select(sockets_list, [], []) 
  

    if len(usr_name) == 0:
        usr_name = input("Please enter your name >>>> ")
        server.send(usr_name.encode(FORMAT))
        ip = 'raj'
    


    for socks in read_sockets:
        if socks == server:
            message = socks.recv(2048).decode(FORMAT)
            print(message)
        else:
            # message = sys.stdin.readline()
            # server.send(message.encode(FORMAT))
            # sys.stdout.write("<You>>> ")
            # sys.stdout.write(message)
            # sys.stdout.flush()
            if(len(ip) > 0 ): 
                server.send(f'{usr_name} joined the party'.encode(FORMAT))
            message = input('')
            server.send(str(message).encode(FORMAT))
            print(f"<YOU>>> {message}")

server.close()
