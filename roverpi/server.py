import nxt.locator
from nxt.motor import *
import socket
import os
import threading
import select
import commands
from BrickCommands import BrickCommands, BrickHelper

"""
    Maneja el servidor.
"""
class Server(threading.Thread):

    def __init__(self, socket_svr):
        threading.Thread.__init__(self)
        self.svrsocket = socket_svr
        self._read_fd, self._write_fd = os.pipe()
        self.clientes = [self._read_fd]
        self.brickHelper = BrickHelper()
        self.cmd = BrickCommands(self.brickHelper.GetAvailableBrick())

    """
        Corre la Logica del Servidor
    """
    def run(self):
        print "Cliente Conectado, corriendo proceso de espera de comandos....."
        salir = False
        while not salir:
            print "A la espera...."
            clientes, b, c = select.select(self.clientes, [], [])
            for cliente in clientes:
                print "Intentando!"
                if (cliente == self._read_fd):
                    if os.read(self._read_fd, 1) == '0':
                        salir = True
                        print "Bye ", cliente[1]
                else:
                    msj = cliente.recv(1024)  #  Recibimos un comando
                    if msj is not None:
                        if msj.startswith("cmd="):
                            print msj[4:]
                            if msj[4:]:
                                self.cmd.forward(self.brickHelper.GetAvailableBrick(), 360)  
                                self.enviarcliente(cliente, "Ola k ase?")
                    salir = True

            if salir:
                self.removeCliente(cliente)
                cliente.close()
    """
        Agrega un response a todos los clientes.
    """
    def enviar(self, emisor, msj):
        for cliente in self.clientes:
            if cliente != self._read_fd:
                cliente.send(mensaje)

    def enviarcliente(self, socket_cliente, msg):
        socket_cliente.send(msg)

    def nuevo_cliente(self, socket_cliente):
        self.clientes.append(socket_cliente)
        os.write(self._write_fd, '1')

    def exit(self):
        os.write(self._write_fd, '0')

    def removeCliente(self, cliente):
        self.clientes.remove(cliente)