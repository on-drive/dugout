# Python program to implement client side of chat room.
import socket
import select
import sys

FORMAT = "utf-8"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP_address = '192.168.36.221'
Port = 5053
server.connect((IP_address, Port))


while True:

    # maintains a list of possible input streams
    sockets_list = [sys.stdin, server]

    read_sockets, write_socket, error_socket = select.select(sockets_list, [], [])

	# usr_name = ''
	# usr_name = input("Please enter your name")
	# server.send(user_name.)
	

    for socks in read_sockets:
        if socks == server:
            message = socks.recv(2048).decode(FORMAT)
            print(message)
        else:
            message = sys.stdin.readline()
            server.send(message.encode(FORMAT))
            sys.stdout.write("<You>")
            sys.stdout.write(message)
            sys.stdout.flush()

server.close()
