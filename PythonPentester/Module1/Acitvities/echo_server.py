#!/usr/bin/env python3
import socket
import sys
import argparse

def server(port):
    host="xx.xx.xx.xx"
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.setsockopt(socket.SOL_SOCKET,
                    socket.SO_REUSEADDR, 1)

    print("Start conection with host: %s  port: %s" %(host, port))
    sock.bind((host, port))
    sock.listen(1)
    print("Wait for connection: ")

    client, address = sock.accept()
    data = client.recv(255)
    print ("Recvied: %s" %data)
    client.send(data)

    print("Bye")
    client.close()


if __name__ == "__main__":
    parse = argparse.ArgumentParser(description="Socket Echo Server")
    parse.add_argument("--port", action="store", dest="port", type=int,
                       required=True)

    arguments = parse.parse_args()
    port = arguments.port
    server(port)
