import numpy

shapes = tuple(map(int,input().split()))

print(numpy.zeros((shapes), dtype=numpy.int))
print(numpy.ones((shapes), dtype=numpy.int))
