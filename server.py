import socket
import threading
import _thread
from _thread import start_new_thread

HEADER = 1024
PORT = 5050
IP_ADD = socket.gethostbyname(socket.gethostname())
ADDR = (IP_ADD, PORT)
FORMAT = "utf-8"
# DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

server.listen(5)

clients_list = []


def handle_client(conn, addr):
    # print(f"[NEW CONNECTION] {addr} connected.")
    conn.send("Welcome to baba ka dugout")
    connected = True
    # while connected:
    #     # msg_length = conn.recv(HEADER).decode(FORMAT)
    #     # if msg_length:
    #     #     msg_length = int(msg_length)
    #     msg = conn.recv(HEADER).decode(FORMAT)
    #     if msg == DISCONNECT_MESSAGE:
    #         connected = False
    #     conn.send(msg.encode(FORMAT))

    while True:
        try:
            msg = conn.recv(HEADER)
            if msg:
                print(f"[{addr} ] - {msg}")
                message_to_send = f"[{addr}] - {msg}"
                broadcast(message_to_send, conn)
            else:
                remove(conn)
        except:
            continue


def broadcast(message, connection):
    for clients in clients_list:
        if clients != connection:
            try:
                clients.send(message)
            except:
                clients.close()
                # if the link is broken, we remove the client
                remove(clients)


def remove(connection):
    if connection in clients_list:
        clients_list.remove(connection)


# def start():
#     server.listen()
#     print(f"[LISTENING] Server is listening on {SERVER}")
#     while True:
#         conn, addr = server.accept()
#         clients_list.append(conn)
#         thread = threading.Thread(target=handle_client, args=(conn, addr))
#         thread.start()
#         print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


# print("[STARTING] server is starting...")
# start()


while True:

    """Accepts a connection request and stores two parameters,
    conn which is a socket object for that user, and addr
    which contains the IP address of the client that just
    connected"""
    conn, addr = server.accept()

    """Maintains a list of clients for ease of broadcasting 
    a message to all available people in the chatroom"""
    clients_list.append(conn)

    # prints the address of the user that just connected
    # print(addr[0] + " connected")

    # creates and individual thread for every user
    # that connects
    start_new_thread(handle_client, (conn, addr))

conn.close()
server.close()
