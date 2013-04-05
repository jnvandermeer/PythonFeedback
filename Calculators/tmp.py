import numpy
def _temporalFilter(vec,filtsize):
    """ Do a temporal filtering of the feedback_rawvalues
        check if the last N digits are not 0
        then return the av. value of those N
    """
    # vec = self.Feedback_rawvalues
    check=True
    for i in range(filtsize):
        if vec[-i-1]==0:
            check=False

    if check:
        return numpy.mean(vec[-3:])
    else:
        return 0    
