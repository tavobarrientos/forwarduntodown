import asyncore
import socket
from BrickCommands import BrickCommands, BrickHelper


class ServerHandler(asyncore.dispatcher_with_send):

	def handle_read(self):
		data = self.recv(1024)
		if data:
			h = BrickHelper()
			brick = h.GetAvailableBrick()
			cmd = BrickCommands(brick)

			print data
			print "Ejecutando comando en el brick %s" % repr(h.GetBrikName(brick))

			if data.startswith("cmd="):
				comando = data[4:]
				executed = cmd.ExecuteCommand(comando)
				self.send(cmd)


class AsyncServer(asyncore.dispatcher):

	def __init__(self, host, port):
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