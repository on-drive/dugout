import socket
import select
import sys

HEADER = 1024
PORT = 5050
FORMAT = "utf-8"
# DISCONNECT_MESSAGE = "!DISCONNECT"
IP_ADD = "192.168.55.221"
ADDR = (IP_ADD, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

# def send(msg):
#     message = msg.encode(FORMAT)
#     # msg_length = len(message)
#     # send_length = str(msg_length).encode(FORMAT)
#     # send_length += b' ' * (HEADER - len(send_length))
#     # client.send(send_length)
#     client.send(message)
#     # rec_add = client.recv(HEADER).decode(FORMAT)


while True:
    sockets_list = [sys.stdin, client]
    read_sockets, write_socket, error_socket = select.select(sockets_list, [], [])

    for socks in read_sockets:
        if socks == client:
            message = socks.recv(HEADER)
            print(message)
        else:
            message = sys.stdin.readline()
            client.send(message)
            sys.stdout.write("<You>")
            sys.stdout.write(message)
            sys.stdout.flush()
client.close()
