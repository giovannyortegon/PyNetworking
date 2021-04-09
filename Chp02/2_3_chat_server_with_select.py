#!/usr/bin/env python3

import select
import socket
import sys
import signal
import pickle
import struct
import argparse

SERVER_HOST = 'localhost'
CHAT_SERVER_NAME = 'server'

# some utilities
def send(channel, *args):
    buffer = pickle.dumps(args)
    value = socket.htonl(len(buffer))
    size = struct.pack("L", value)
    channel.send(size)
    channel.send(buffer)


def receive(channel):
    size = struct.calcsize("L")
    size = channel.recv(size)

    try:
        size = socket.htohl(struct.unpack("L", size)[0])
    except struct.error as e:
        return ''

    buf = ""

    while len(buf) < size:
        buf = channel.recv(size - len(buf))
    return pickle.loads(buf)[0]

class ChatServer:
    """ An example char server using select """
    def __init__(self, port, backlog=5):
        self.clients = 0
        self.clientmap = {}
        self.outputs = []       # list output sockets

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((SERVER_HOST, port))
        print("Server listening to port: %s ..." %port)

        self.server.listen(backlog)

        # Catch keyboard interrupts
        signal.signal(signal.SIGINT, self.sighandler)


    def sighandler(self, signum, frame):
        """ Clean up client outputs """
        # Close the server
        print("Shutting down server...")

        # Close existing client socket
        for output in self.outputs:
            outputs.close()

        self.server.close()


    def get_client_name(self, client):
        """ Return the name of the client """
        info = self.clientmap[client]
        host, name = info[0][0], info[1]

        return '@'.join((name, host))


    def run(self):
        inputs = [self.server, sys.stdin]
        self.outputs = []
        running = True

        while running:
            try:
                readable, writeable, exceptional = select.select(inputs,
                                                                 self.outputs,
                                                                 [])
            except select.error as e:
                break

            for sock in readable:
                if sock == self.server:
                    # handle the server socket
                    client, address = self.server.accept()
                    print("Chat server: got connect %d from %s" %
                         (client.fileno(), address))
                    # Read the login name
                    cname = receive(client).split("NAME: ")[1]

                    # Compute client name and send back
                    self.clients += 1
                    send(client, "CLIENT: " + str(address[0]))
                    inputs.append(client)
                    self.clientmap[client] = (address, cname)

                    # Send joining information to other clients
                    msg = "\n(Connected: New client (%d) from %s)" %
                             (self.clients, self.get_client_name(client))

                    for output in self.outputs:
                        send(output, msg)

                    self.outputs.append(client)

                elif sock == sys.stdin:
