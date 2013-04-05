# This script will run a simple feedback based on the output in the
# feedback folder of TBV.

import site
import easygui
import time
UPDATE_INTERVAL=0.05

basedir = '/home/brain/PythonFeedback/'
site.addsitedir(basedir + 'PathWatcher/')
site.addsitedir(basedir + 'TCPIPTraffic/')
site.addsitedir(basedir + 'DataTrackers/')
site.addsitedir(basedir + 'Calculators/')
site.addsitedir(basedir + 'myFileIO/')


from PathWatcher import PathWatcher
from DataTrackers import rtpDataTracker
from myClient import myClient
from TwoROIDiff import TwoROIDiff
from myFileIO import *



# initialization stuff:
# we could do this in another object, but for now we let it remain here.
server_address=raw_input('Please specify server address [[localhost]]: ')
if server_address == '':
    server_address = 'localhost'
    
port_number=raw_input('Please specify server address [[32701]]: ')
if port_number == '':
    port_number = '32701'
port_number = int(port_number)

print 'Please specify which directory to watch: '
directory_to_watch=easygui.diropenbox()

regex=raw_input("Please tell me what the regex is [['.*rtp$']]: ")
if regex == '':
    regex = '.*rtp$'




# this instantiates our watcher
watcher=PathWatcher(directory_to_watch,regex)

# our container for keeping a record of the data
tracker=rtpDataTracker()

# the way we would like to process the data.
calc = TwoROIDiff()
# 2roicalculator.init(training=30,...)

# this is our nice little client (to send stuff),
client=myClient(server_address, port_number)



while True:

    if watcher.isAdded():
        if len(watcher.added) == 1:

            # add data from the new file...
            tracker.update(watcher.added[0])

            # update/process
            percentage = calc.process(tracker)

            # send the percentage score.
            client.sendInt(percentage)

        # some logic to process weird occurences of too many/few files...
        elif(len(watcher.added)) == 0:
            print 'No New Feedback Files..'
            # maybe raise some error?
        elif(len(watcher.added)) > 1:
            print 'Too many Feedback Files..'

    
    time.sleep(UPDATE_INTERVAL)
    




