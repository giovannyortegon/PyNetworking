#!/usr/bin/env python3
import socket
import sys
import argparse

def client(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_addr = (host, port)
    print("Connect to %s port %s" % server_addr)
    sock.connect(server_addr)
    print("Connected")

    message = "My host name is: "+ socket.gethostname()
    sock.sendall(message.encode("utf-8"))
    rev_msg = sock.recv(255)
    print("Recived: %s" %rev_msg)

    print("Bye")
    sock.close()

if __name__ == "__main__":
    parse = argparse.ArgumentParser(description="Socket echo client")
    parse.add_argument("--host", action="store", dest="host", required=True)
    parse.add_argument("--port", action="store", dest="port", type=int,
                       required=True)

    arguments = parse.parse_args()
    host = arguments.host
    port = arguments.port
    client(host, port)
