#!/usr/bin/env python

"""
a simple echo-server
"""

import socket

HOST = 'localhost'
PORT = 50000
BUFF = 1024
ADDR = (HOST, PORT)
running = 1

#creates a server side socket and bind the socket to the host and port
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(ADDR)
server_socket.listen(2) # can keep 2 clients waiting while serving current client

#listens for incoming requests
while running:
	print 'waiting for connection...'
	client_socket, addr = server_socket.accept()
	print '...connected from:', addr

	#client receives data and echoes it back 
	while running:
		data = client_socket.recv(BUFF)
		if not data: break	#stops when client doesn't send data
		client_socket.send(data) #echoes data back to client
	client_socket.close()
server_socket.close()
