#!/usr/bin/python
import nxt.locator
from roverpi.server import Server
from roverpi.AsyncServer import AsyncServer
import socket
import asyncore

def main():
	try:
	    print "Iniciando servidor....."
	    svr = AsyncServer('', 8000)
	    asyncore.loop()
	except KeyboardInterrupt:
		print "Bye"

if __name__ == "__main__":
    main()
