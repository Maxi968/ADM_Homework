import numpy
numpy.set_printoptions(legacy='1.13')

N, M = tuple(list(map(int, input().split())))

print(numpy.eye(N, M, k=0))
