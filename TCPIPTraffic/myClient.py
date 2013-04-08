import socket
import sys
import easygui


class myClient(object):

    """
    Anther hopefully very simple sender class.
    Upon initialization, it will ask for an address and a port.
    Then, it will send text or whatever.

    *args = 'ip' as string, port as int.
    
    """
    

    def __init__(self,*args):

        if not args:
            ip_address=easygui.textbox(msg='Enter ip address', title = 'ip')
            ip_address=ip_address[:-1]

            port=easygui.textbox(msg='Enter port number (32701)', title = 'port (32701)')
            port=port[:-1]
            port=int(port)
        else:
            ip_address=args[0]
            port=args[1]

        self.ip_address=ip_address
        self.port=port
        self.server_address = (ip_address, port)
        
    def makeSock(self):
        """
        Makes the socket specified with this object's properties.
        """
        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect the socket to the port on the server given by the caller
        print >>sys.stderr, 'connecting to %s port %s' % self.server_address
        sock.connect(self.server_address)
        return sock


    def sendInt(self,number):
        """
        This should send an int number... maybe I can send dicts, too...
        but for that I would need another function.
        """
        try:
            sock=self.makeSock()
            message = '%16s' % number
            print >>sys.stderr, 'sending "%s"' % message
            # according to Thijs, this is called 'pushing' the data.
            sock.sendall(message)
            sock.close()
        except:
            print "Cannot send... server is probably not running!"

