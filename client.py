import socket
import select
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if len(sys.argv) != 2:
    print("Correct usage: script, IP address, port number")
    exit()
IP_address = socket.gethostbyname(socket.gethostname())
Port = int(sys.argv[1])
server.connect((IP_address, Port))
ip_name_dict = {}

while True:

    # maintains a list of possible input streams
    sockets_list = [sys.stdin, server]

    """ There are two possible input situations. Either the
	user wants to give manual input to send to other people,
	or the server is sending a message to be printed on the
	screen. Select returns from sockets_list, the stream that
	is reader for input. So for example, if the server wants
	to send a message, then the if condition will hold true
	below.If the user wants to send a message, the else
	condition will evaluate as true"""
    read_sockets, write_socket, error_socket = select.select(
        sockets_list, [], [])

    for socks in read_sockets:
        if socks == server:
            message = socks.recv(1024).decode('utf-8')
            print(message)

        else:

            try:
                user_name = input("")
                ip_name_dict[IP_address] = user_name.splitlines()[0]
            except:
                user_name = ip_name_dict[IP_address]

            server.send(user_name.encode('utf-8'))

            message = input("enter your message")
            server.send(message.encode('utf-8'))
            print(ip_name_dict[IP_address]+" - "+message)

            # sys.stdout.flush()
server.close()
