# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import socket
import sys

# <codecell>

sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# <codecell>

server_address = ('localhost', 10000)

# <codecell>

print >> sys.stdout, 'starting up on %s port %s' % server_address

# <codecell>

sock.bind(server_address)

# <codecell>

sock.listen(1)
while True:
    print >> sys.stderr, 'waiting for connection'
    connection, client_address=sock.accept()
    
    
    try:
        print >>sys.stderr, 'connection from', client_address

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print >>sys.stderr, 'received "%s"' % data
            if data:
                print >>sys.stdout, 'sending data back to the client'
                connection.sendall(data)
            else:
                print >>sys.stdout, 'no more data from', client_address
                break
            
    finally:
        # Clean up the connection
        connection.close()

# <codecell>


