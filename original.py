#!/usr/bin/python
import nxt.locator
from roverpi.server import Server
from roverpi.AsyncSocket import *
import socket

def main():
    print "Iniciando servidor....."
    socket_server = socket.socket()
    socket_server.bind((socket.gethostname(), 8000))
    socket_server.listen(5)
    server = Server(socket_server)
    # server.run()
    print "Server listo, esperando conexiones."
    while 1:
        try:
            socket_cliente, datos_cliente = socket_server.accept()
            if socket_cliente is not None:
                server.enviar("server", datos_cliente[0] + ":" + str(datos_cliente[1]) + " se a conectado.")
                server.nuevo_cliente(socket_cliente)
                server.run()
        except KeyboardInterrupt:
            print "Interrumpiste la ejecucion del server"
            server.exit()
            break 
        except nxt.locator.BrickNotFoundError:
            print "No hay Brick conectado..."
            server.exit()
            break
        except Exception as e:
            print e
            server.exit()
            break
    print "Cerrando..."
    server.exit()
    socket_server.close()

if __name__ == "__main__":
    main()