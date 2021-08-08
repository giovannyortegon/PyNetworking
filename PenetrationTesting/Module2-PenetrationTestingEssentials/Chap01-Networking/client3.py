#!/usr/bin/env python
import socket

host = "127.0.0.1"
port = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

buf = bytearray("-" * 30)			# buffer created
print("Number of bytes ", s.recv_into(buf))
print(buf)

s.close()
