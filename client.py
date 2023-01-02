#!/usr/bin/python3

import socket

clientsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # Instantiates a socket object for IPv4 and which requires a handshake (because TCP)

host = socket.gethostbyname() # Specify this client's host IP
port = 6666 # specifies port to use for establishing connection to server

clientsocket.connect((host,port)) # Adds these specifications to our socket object

message = clientsocket.receive(1024) # stores the message received from server, int specifies buffer size limit we will accept for messages from server

clientsocket.close() # closes connection to server

print(message.decode('ascii')) # prints mesage, by first decoding it since it was transmitted encoded with ASCII

