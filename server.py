#!/usr/bin/python
import nxt.locator
from roverpi.server import Server
from roverpi.AsyncServer import AsyncServer
import socket
import asyncore

def main():
    print "Iniciando servidor....."
    svr = AsyncServer(socket.gethostname(), 8000)
    asyncore.loop()

if __name__ == "__main__":
    main()