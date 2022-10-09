import numpy

N, M = tuple(map(int, input().split()))

matrix=[]

for _ in range(N):
    row = list(map(int, input().split()))
    matrix.append(row)

sum_matr = numpy.sum(matrix, axis=0)
print(numpy.prod(sum_matr))
