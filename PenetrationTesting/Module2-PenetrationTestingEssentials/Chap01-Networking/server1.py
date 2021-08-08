#!/usr/bin/env python
import socket

host = "127.0.0.1"			# server address
port = 12345				# port of server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))		# bind to server
s.listen(2)

try:
	conn, addr = s.accept()
	print(addr, " Now connected")
	conn.send("Thanks you for connecting")
except Exception as e:
	print(e)
finally:
	conn.close()
	s.close()
