#!/usr/bin/python3

import socket;

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # instantiates a socket object, specifying the protocol and communication type. For IPv6 use AF_INET6

host = socket.gethostname() # specifies host to listen from, in this case we use the built-in method to retrieve the IP of this server, which returns the addr as a str
port = 444 # specifies port to listen for inbound connections on

serversocket.bind((host,port)) # binds these specifications to the socket object we created

serversocket.listen(3) # int specifies the MAX number of connections we will permit at any given time.

print("Server ready. Awaiting connection with a client...")

while True:

    clientsocket, address = serversocket.accept() # accept receives address information from the client

    print("Connection received from %r" % str(address))

    message = "Connection established! Thank you for connecting to the server." + "\r\n"

    clientsocket.send(message.encode('ascii')) # encodes ASCII char of our string above and transmits it to the connected client

    clientsocket.close() # closes the established connection
