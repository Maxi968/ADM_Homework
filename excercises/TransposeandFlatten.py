import numpy

N, M = tuple(map(int, input().split()))

matrix = []

for _ in range(N):
    column = list(map(int, input().split()))
    matrix.append(column)

np_arr = numpy.array(matrix)
print(numpy.transpose(np_arr))
print(np_arr.flatten())
    
    
         
