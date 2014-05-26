# jacTalk Server
# developed by @jaccon
# Last update 26/05/2014

import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address given on the command line
server_address = ('',1309)
sock.bind(server_address)
print >>sys.stderr, 'Iniciando jTalk em %s port %s' % sock.getsockname()
sock.listen(1)

while True:
    print >>sys.stderr, 'Aguardando novas conexoes...'
    connection, client_address = sock.accept()
    try:
        print >>sys.stderr, 'cliente conectado:', client_address
        while True:
            data = connection.recv(16)
            print >>sys.stderr, 'recebido... "%s"' % data
            if data:
                connection.sendall(data)
            else:
                break
    finally:
        connection.close()
