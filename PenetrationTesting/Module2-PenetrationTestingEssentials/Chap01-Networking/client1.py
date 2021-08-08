#!/usr/bin/env python
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
port = 12345

try:
	s.connect((host, port))
	print(s.recv(1024))
	s.send("Hello Server")
except Exception as e:
	print(e)
finally:
	s.close()
