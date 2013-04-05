import numpy

class TwoROIDiff(object):
    """
    Input: a tracker (of data)
    Output: a 2-ROI-diff.

    The data in the tracker should contain at least 2 columns... at some point
    during the measurement, for at least ~20 data points.

    This one is called incrementally!
    """

    def __init__(self):
        """
        set some default values...
        """
        self.training_size = 20
        self.mode = 'training'

        # could be set to something else?
        self.Feedback_stdsIn100Percent = 6
        self.Feedback_startpoint = 50

        # keep track of the feedback values
        self.Feedback_rawvalues = []
        self.Feedback_returnvalues = []

        # specify some filtering value; to stop jittering.
        self.Feedback_tFilterSize = 3

                 
        
    #def init(self,training_size):
    #    """ I want its own initialization routine to set all the variables.
    #    """
    #    self.


    def process(self,tracker):
        """ receives a tracker.
            Queries it... and calculates a percentage score.
            returns the percentage value.
        """


        # only do something once we've selected 2 ROIs.
        if len(tracker.ConsecutiveCheck)>=2:
            
            # determine if we are in training mode
            if self.mode == 'training':
                self._trainingMode(tracker)

            # or in feedback mode
            elif self.mode == 'feedback':
                self._feedbackMode(tracker)


            elif self.mode == 'calculation':
                self._calculationMode(tracker)


            if self.mode == 'feedback':
                Feedback_value = self.return_value
            else:
                Feedback_value = 0

        else:
            Feedback_value =0


        self.Feedback_rawvalues.append(Feedback_value)


        


        # if in training mode, then gather data until check > 30

        # then switch to calculation, which then switches to feedback mode

        # if in feedback mode, do the actual feedback, as long as check > 30

        # if it is < 30, switch back to training mode.

        # a helpere function to do filtering, within process.
        def temporalFilter(vec,filtsize):
            """ Do a temporal filtering of the feedback_rawvalues
                check if the last N digits are not 0
                then return the av. value of those N
            """
            # vec = self.Feedback_rawvalues
            check=True

            if len(vec) >=filtsize:
                for i in range(filtsize):
                    if vec[-i-1]==0:
                        check=False

                if check:
                    return numpy.mean(vec[-3:])
                else:
                    return 0
            else:
                return 0
        
        # apply a (temporal) filter of (some) points...
        val = temporalFilter(self.Feedback_rawvalues,self.Feedback_tFilterSize)
        self.Feedback_returnvalues.append(val)

        return int(val)
        


    # helper functions.
    def _feedbackMode(self,tracker):
        """ This function should return a percentage based on the
            last data point found in tracker, and stuff in self.params
            as long as tracker.ConsecutiveCheck
        """

        if tracker.ConsecutiveCheck[0]>=self.training_size and tracker.ConsecutiveCheck[1]>=self.training_size:
            # writing it out like this seems a bit too much, but still..
            # it could be a thing to do.
            s_roi1 = tracker.data[0][-1]
            s_roi2 = tracker.data[1][-1]
            
            diff_sig = s_roi1 - s_roi2

            self.diff_sig = diff_sig


            
            # where do we begin? (50%?)
            b = self.Feedback_startpoint

            stdfac = self.Feedback_stdsIn100Percent

            diff_std = self.diff_std

            diff_mean = self.diff_mean

            feedback_sig = b + 100 / ( diff_std * stdfac) * (diff_sig - diff_mean)

            self.return_value = feedback_sig
        else:
            self.mode = 'training'
            
            self.process(tracker)




    # helper function, II
    def _calculationMode(self,tracker):
        """ Do the necessary calculations
            Set a dict with the necessary values in self.params
            Hmm... well, the dict didn't go through after all! Doh.
            Set the mode to feedback, call self.process
        """

        # get the last # of point of the data
        roi1 = tracker.data[0][-self.training_size:]
        roi2 = tracker.data[1][-self.training_size:]

        mean_roi1 = numpy.mean(roi1)
        mean_roi2 = numpy.mean(roi2)

        std_roi1 = numpy.std(roi1)
        std_roi2 = numpy.std(roi2)

        diff_std = pow((pow(std_roi1,2) + pow(std_roi2,2)),0.5)
        diff_mean = mean_roi1 - mean_roi2
        
        # update the params dict
        self.diff_std = diff_std
        self.diff_mean = diff_mean

        self.mode = 'feedback'
        self.process(tracker)
        
        


    # one underscore, or two??
    def _trainingMode(self,tracker):
        """ just gather data...
            When the counter reaches self.training_size, set the mode to calculation
            and call self.process
            This function could return a -100 (code for bein in training)
        """
        
        if tracker.ConsecutiveCheck[0]>=self.training_size and tracker.ConsecutiveCheck[1]>=self.training_size:
            # call self.process
            self.mode = 'calculation'
            self.process(tracker)

        else:
            # do nothing!
            # or maybe set a return value of -100
            self.return_value = -100
        
