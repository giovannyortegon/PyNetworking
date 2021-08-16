#!/usr/bin/env python
import socket

host = "192.168.1.50"
port = 12346

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
	s.bind((host, port))
	s.settimeout(5)

	data, addr = s.recvfrom(1024)

	print "Received from: ", addr
	print "Obtained: ", data

	s.close()
except socket.timeout:
	print "Client not connected"
	s.close()
