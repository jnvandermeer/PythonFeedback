import io
import re

def rtpFileInterpreter(infile):
    """
    Opens a file (infile), and does something with it. Returns a feedback value
    (in this case an int)
    """
    # self-exemplanory
    f=open(infile,'r')
    data=f.read().split()
    f.close()

    return int(data[0])


