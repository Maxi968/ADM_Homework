import numpy

def arrays(arr):
    a = numpy.array(arr, float)
    return numpy.array(list(reversed(a)))

