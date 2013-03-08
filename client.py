#!/usr/bin/env python

"""
a simple client
"""

import socket

HOST = 'localhost'
PORT = 50000
BUFF = 1024
ADDR = (HOST, PORT)
running = 1

#creates a client side socket and connect
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(ADDR)

#listens for incoming requests
while running:
	data = raw_input('> ')
	if not data: break			
	client_socket.send(data)	#sends data to server
	data = client_socket.recv(BUFF)	#received echoed data from server
	if not data: break
	print data

client_socket.close()