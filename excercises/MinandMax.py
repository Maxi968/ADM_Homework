import numpy

N, M = tuple(map(int, input().split()))

matrix = []

for _ in range(N):
    row = list(map(int, input().split()))
    matrix.append(row)
    
min_matr = numpy.min(matrix, axis=1)
print(numpy.max(min_matr))

