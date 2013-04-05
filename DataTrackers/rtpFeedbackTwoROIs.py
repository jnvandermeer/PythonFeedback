# numpy is difficult to use with appending lists... so, we will use
# instead python's own built-in lists for the job.
# probably there are some ways to make numpy lists also work.
# but this is another matlab thing that translates badly.

# but... we need numpy for referencing like in a 2D matrix... so import it
# anyway. the good thing is that the update method is fast, and you only
# create the numpy array when you need it. Which probably saves some computational
# time, if I have to believe the python documentation.

import numpy

class DataTracker(object):
    """
    It tracks data when you call its update method. It puts
    it into array, a python array that dynamically changes with each
    call to 'update'.
    The other feedback things are a sub-class of this one.
    # maybe, some plotting function could be a superclass of this one, too.

    rtpDataArray is a subclass of this one, because you insert a file (instead of data)
    update now is a method that will be overloaded.
    # the old method can still be called, however, but the overloading method.


    useful trackers:
    1) ConsecutiveCheck = now many times something has been written to the data.
    2) nvec = number of vectors in the data.
    """

    def __init__(self):

        # i need to keep track how many times the update method has been called.
        self.update_times_called = 0

        # a list, a container for my data
        self.data=[]

        # this counter should list how many times the data was NOT None for each column in data.
        self.ConsecutiveCheck = []

        # this keeps track of how many voxels/ROIs are there in the last call.
        self.nvec = 0
        
        self.ncols = 0

        # maybe it's better if I make a method of the above variables??
        # could discuss with a python or OO Expert.
        # or look it up myself.
        # or use the name mangling to keep things more hidden
        # so that I don't accidentally override it later on.
        # or even have to worry about that!!!

    def update(self,vector):
        """
        This update method should NOT return anything
        but keeps track of data, a 2D array.
        vector MUST be a list.
        with rows = #ROIs
        with cols = #timepoints
        It puts the values from vector into this data, so that later on
        when you call data, you can do all kinds of neat-o operations on it.

        UPDATE... it seems to be quite incredibly robust. vector can be a
        list of ANYTHING!!!
        """

        # but also should keep in mind self.update_times_called!!!
        self.update_times_called+=1

        # assume that data is a list!

        # asses the # of elements in vector
        nelements=len(vector)

        # yeah, keep track.
        self.nvec = nelements

        # find out the # of cols in self.data
        if self.data:
            ncols=len(self.data[0])
        else:
            ncols=0

        # might as well store that, too.
        self.ncols = ncols

        # if the # of elements is < than the colsize, append the elements with None
        if nelements<ncols:
            for i in range(ncols-nelements):
                vector.append(None)

        # if the # of elements is > than colsize, append new cols in list
        if nelements>ncols:
            for item in self.data:
                for i in range(nelements-ncols):
                    item.append(None)
            


        # if the # of elements is equal to the colsize, append in list
        # no check, because this should always be true.
        self.data.append(vector)

        # do some logic to keep track of now many consecutive data points we
        # have up to this point
        # this is handy for triggering certain calculations
        # later on.
        # print vector
        # uses ncols...
        # probably, this code can be re-written a thousand times more
        # beatiful.
        if nelements == 0:
            self.ConsecutiveCheck = []
            for i in range(ncols):
                self.ConsecutiveCheck.append(0)
                
        elif nelements<ncols:

            # still do this one, always...
            for i in range(ncols):
                self.ConsecutiveCheck[i] += 1
            
            for i in range(1,ncols-nelements+1):
                self.ConsecutiveCheck[-i]=0

        elif nelements>ncols:
            # still add to the existing columns...
            for i in range(ncols):
                self.ConsecutiveCheck[i] += 1
            
            for i in range(nelements-ncols):
                self.ConsecutiveCheck.append(1)

        else:
            # add 1 to all the stuff... but ONLY for the things
            # we have any data on.
            # if input is the same, add...
            for i in range(nelements):
                self.ConsecutiveCheck[i] += 1


            

    def __str__(self):
        # borrow from the list the print function!
        s=list.__str__(self.data)
        return s
        

    def getData(self):
        """
        returns the stored list-of-lists as a numpy array.
        A bit unwieldy, but it works.
        It's probably a good idea to just call this method only once.
        """
        return numpy.array(self.data)




class rtpDataTracker(DataTracker):
    """
    A sub-class of DataArray, this one reads in files to update.
    """

    def __init__(self):
        """
        some rtp-specific stuff:
        The first number is the # of ROIs
        The last number is either None, or the current condition
        """
        self.nrois = []
        self.condition = []

        # call the parent init method.
        DataTracker.__init__(self)
        
    def update(self,infile):
        """
        An over-loading method... this one accepts a string, which should
         be some path-to-a-file! .. and then converts
        the data points to a vector... and then calls the update method of
        the parent

        This subclass just deals with the conversion from the file into a vector
        of numpy.floats32's.
        """
        f=open(infile,'r')
        vector=f.read().split()
        f.close()

        # convert to floats (everything!), it's easier.
        newvec=[numpy.float32(item) for item in vector]


        #rtp-file-specific stuff.
        
        # convert to first one to an INT!!
        # print newvec
        newvec[0]=int(newvec[0])

        # do the last number..
        if newvec[0] == 0:
            self.condition.append(None)

        if newvec[0] > 0:
            self.condition.append(int(newvec.pop(-1)))


        # keep track of which condition it is in a SEPARATE array!
        # and pop it off.
        self.nrois.append(newvec.pop(0))
        

        # it's easier than you think!
        # calling the overridden method!!
        DataTracker.update(self,newvec)


