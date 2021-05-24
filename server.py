# Python program to implement server side of chat room.
import socket
import select
import sys
from _thread import *

HEADER = 1024
PORT = 5053
IP_ADD = socket.gethostbyname(socket.gethostname())
ADDR = (IP_ADD, PORT)
FORMAT = "utf-8"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# takes the first argument from command prompt as IP address
IP_address = IP_ADD

# takes second argument from command prompt as port number
Port = PORT

server.bind((IP_address, Port))


server.listen(2)

list_of_clients = []
client_names = []

def clientthread(conn, addr):

	# sends a message to the client whose user object is conn
	# conn.send(f"Hola {user_name}!! Hope you brought some pizzas.".encode(FORMAT))
	
	conn.send(f"Hola!! Hope you brought some pizzas.".encode(FORMAT))
	user_name = conn.recv(2048).decode(FORMAT)


	while True:
			try:
				message = conn.recv(2048).decode(FORMAT)
				if message:
					print ("<" + addr[0] + "> " + message)
					# Calls broadcast function to send message to all
					message_to_send =( "<" + user_name + "> " + message).encode(FORMAT)
					broadcast(message_to_send, conn)

				else:
					remove(conn)

			except Exception as e:
				print(e)

def broadcast(message, connection):
	for clients in list_of_clients:
		if clients!=connection:
			try:
				clients.send(message)
			except:
				clients.close()
				# if the link is broken, we remove the client
				remove(clients)

def remove(connection):
	if connection in list_of_clients:
		list_of_clients.remove(connection)

while True:
	conn, addr = server.accept()
	list_of_clients.append(conn)

	# prints the address of the user that just connected
	print (addr[0] + " connected")

	# creates and individual thread for every user
	# that connects
	start_new_thread(clientthread,(conn,addr))	

conn.close()
server.close()
