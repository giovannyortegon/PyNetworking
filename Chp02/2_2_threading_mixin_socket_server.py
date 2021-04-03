#!/usr/bin/env python
import os
import socket
import threading
import socketserver

SERVER_HOST = 'localhost'
SERVER_PORT = 0
BUF_SIZE = 1024

def clients(ip, port, message):
    """ A client to test threading mixin server """
    # connect to server
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))

    try:
        sock.sendall(bytes(message, 'utf-8'))
        response = sock.recv(BUF_SIZE)
        print("Client received: %s" %response)
    finally:
        sock.close()

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    """ An example of threaded TCP request handler """
    def handle(self):
        data = self.request.recv(1024)
        cur_thread = threading.current_thread()
        response = "%s: %s" %(cur_thread.name, data)
        self.request.sendall(bytes(response, 'utf-8'))


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    """ Nothing to add here, inherited everything necessary from parents """
    pass

if __name__ == "__main__":
    # run server
    server = ThreadedTCPServer((SERVER_HOST, SERVER_PORT),
                               ThreadedTCPRequestHandler)
    ip, port = server.server_address # retrive ip address
    # start a thread with the server -- one thread per request
    server_thread = threading.Thread(target=server.serve_forever)
    # Exit the server thread when the main thread exist
    server_thread.daemon = True
    server_thread.start()
    print("Server loop running on thread: %s" %server_thread.name)
    # run clients
    clients(ip, port, "Hello from client 1")
    clients(ip, port, "Hello from client 2")
    clients(ip, port, "Hello from client 3")
    # Server cleanup
    server.shutdown()
