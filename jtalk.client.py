import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port on the server given by the caller
server_address = (sys.argv[1],1309)
print >>sys.stderr, 'Conectando em %s port %s' % server_address
sock.connect(server_address)

try:
    
    message = sys.argv[2]
    print >>sys.stderr, 'enviando... "%s"' % message
    sock.sendall(message)

    amount_received = 0
    amount_expected = len(message)
    while amount_received < amount_expected:
        data = sock.recv(128)
        amount_received += len(data)
        print >>sys.stderr, 'recebido "%s"' % data

finally:
    sock.close()
