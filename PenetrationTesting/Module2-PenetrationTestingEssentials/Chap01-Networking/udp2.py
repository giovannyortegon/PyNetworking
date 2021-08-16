#!/usr/bin/env python
import socket

host = "192.168.1.50"
port = 12346

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print s.sendto("Hello all", (host, port))

s.close()
