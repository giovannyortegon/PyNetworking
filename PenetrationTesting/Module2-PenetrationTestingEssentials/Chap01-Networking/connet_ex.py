#!/usr/bin/env python
import socket

rmip = "127.0.0.1"
portlist = [22, 23, 80, 912, 135, 445, 20]

for port in portlist:
	socks = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	result = socks.connect_ex((rmip, port))
	print port, " : ", result

	socks.close()
