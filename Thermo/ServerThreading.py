import threading
import sys
import socket

class ServerModeBackground(threading.Thread):
    def __init__(self,server_address):
        threading.Thread.__init__(self)
        self.server_address = server_address
        self.data=0

        

    def run(self):

        
        print >>sys.stderr, 'starting up on %s port %s' % self.server_address


        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(self.server_address)
        sock.listen(1)


        try:

            # Just keep it runnin'!! :-)
            while True:

                # this just waits until a thing happens to come along!!!
                connection, client_address = sock.accept()

               
                # print >>sys.stderr, 'client connected:', client_address

                data = connection.recv(16)
                # while data:
                # print >>sys.stderr, 'client connected:', client_address
                # print data
                self.data=int(data)
                
                if self.data==-1:
                        break
                
        finally:        
            connection.close()
            self.__init__(self.server_address)

            


        

        

        

        
