import socket

HEADER = 1024
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.55.221"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    # msg_length = len(message)
    # send_length = str(msg_length).encode(FORMAT)
    # send_length += b' ' * (HEADER - len(send_length))
    # client.send(send_length)
    client.send(message)
    # rec_add = client.recv(HEADER).decode(FORMAT)
    rec_message = client.recv(HEADER).decode(FORMAT)
    print(  ADDR +rec_message )



while True: 
    user_message = input()
    send(user_message)

recv_msg = client.recv(HEADER).decode(FORMAT)
# print(recv_msg)

send(DISCONNECT_MESSAGE)
