import threading
import sys
import socket

class ServerModeBackground(threading.Thread):
    """
    ServerModeBackground starts a new thread, and stores in data the value
    send by the client.
    I made this one to keep the Thermo event loop running!!

    self.data yields the int that you sent..

    server_address = (localhost,port), a tuple.
    
    """
    def __init__(self,server_address):
        threading.Thread.__init__(self)
        self.server_address = server_address
        self.data=0

        

    def run(self):

        
        print >>sys.stderr, 'starting up on %s port %s' % self.server_address


        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(self.server_address)
        sock.listen(1)


        # pff, now I finally got it!
        try:

            # Just keep it runnin'!! :-)
            while True:

                # this just waits until a thing happens to come along!!!
                connection, client_address = sock.accept()

               
                # print >>sys.stderr, 'client connected:', client_address

                data = connection.recv(16)
                # while data:
                # print >>sys.stderr, 'client connected:', client_address
                print data
                self.data=int(data)
                
                if self.data==-1:
                        break
                
                
        connection.close()
        # if I wanted to start it up again!!
        # self.__init__(self.server_address)

            


        

        

        

        
