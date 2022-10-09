import numpy

inp = input().split()
arr = list(map(int, inp))

np_arr = numpy.array(arr)

print(numpy.reshape(np_arr, (3,3)))





