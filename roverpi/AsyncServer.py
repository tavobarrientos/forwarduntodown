import asyncore
import socket
from BrickCommands import BrickCommands, BrickHelper

from threading import Thread


class ServerHandler(asyncore.dispatcher_with_send):

	def handle_read(self):
		data = self.recv(1024)
		if data:
			try:
				h = BrickHelper()
				brick = h.GetAvailableBrick()
				cmd = BrickCommands(brick)


				if data.startswith("cmd=") and len(data) > 4:
					comando = data[4:]
					if comando is not None:
						executed = cmd.ExecuteCommand(comando)
						self.send("OK")
				self.close()
			except Exception as e:
				print e
				self.send("Error")
				self.close()
			


class AsyncServer(asyncore.dispatcher):

	def __init__(self, host='', port=8000):
		asyncore.dispatcher.__init__(self)
		self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
		self.set_reuse_addr()
		self.bind((host, port))
		self.listen(2)
	
	def handle_accept(self):
		pair = self.accept()
		if pair is not None:
			sock, addr = pair
			print "Incoming connection from %s" % repr(addr)
			handler = ServerHandler(sock)