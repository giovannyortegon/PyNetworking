#!/usr/bin/env python
import socket

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#tcp_scoket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

tcp_socket.bind(("localhost", 8080))
tcp_socket.listen(2)

print "Waiting for a Client ..."
(client, (ip, sock)) =  tcp_socket.accept()

print "Received connectiong from: ", ip
print "Start ECHO output ..."

data = "dummy"

while len(data):
    data = client.recv(2048)
    print "Client sent: ", data
    client.send(data)

print "Closing conenction ..."
client.close()
