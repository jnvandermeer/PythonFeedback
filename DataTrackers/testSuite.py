from scipy import *
from pylab import *

import site
basedir = '/home/brain/PythonFeedback/'
site.addsitedir(basedir + 'PathWatcher/')
site.addsitedir(basedir + 'TCPIPTraffic/')
site.addsitedir(basedir + 'DataTrackers/')
site.addsitedir(basedir + 'Calculators/')
site.addsitedir(basedir + 'myFileIO/')


from PathWatcher import PathWatcher
from DataTrackers import rtpDataTracker
from myClient import myClient
from TwoROIDiff import *
from myFileIO import *


# make sure that this one is actually mounted!!
base='/mnt/e/Dropbox/OnderzoeksPlan/RtfMRI_Sessions/ExampleSessions/TBV_FacesHouses/feedback/HousesFaces2'

fl = [base + '-%d' % i + '.rtp' for i in range(1,109)]

tracker=rtpDataTracker()
calc = TwoROIDiff()


feedback_list = []
for f in fl:
    tracker.update(f)
    feedback_value = calc.process(tracker)
    feedback_list.append(feedback_value)
    
    # print tracker.ConsecutiveCheck

    
m=tracker.getData()

plot(calc.Feedback_returnvalues)
plot(calc.Feedback_rawvalues)
show()


##figure(1)
##plot(m[-86:,:])
##title('Time Courses of 2 ROIs')
##xlabel('Time Point (TR = 2sec)')
##ylabel('(Av. (??)) Signal in ROI')
### show()
##
##tracker2=rtpDataTracker()
##
##for f in fl[10:40]:
##    tracker2.update(f)
##
##
##calc = TwoROIDiff()
##
##
##figure(2)
##plot(tracker.data[1][-calc.training_size:])
##plot(tracker.data[0][-calc.training_size:])
##title('Time Courses of 2 ROIs')
##xlabel('Time Point (TR = 2sec)')
##ylabel('(Av. (??)) Signal in ROI)')


