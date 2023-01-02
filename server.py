#!/usr/bin/python3

import socket;

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # instantiates a socket object, specifying the protocol and communication type. For IPv6 use AF_INET6

host = socket.gethostbyname() # specifies host to listen from
port = 666 # specifies port to listen for inbound connections on

serversocket.bind((host,port)) # binds these specifications to the socket object we created

serversocket.listen(3) # int specifies the MAX number of connections we will permit at any given time.

while True:
    clientsocket, address = serversocket.accept() # accept receives address information from the client

    print("Connection received from " % str(address))

    message = "Connection established! Thank you for connection to the server." + "\r\n"

    clientsocket.close() # closes the established connection.
