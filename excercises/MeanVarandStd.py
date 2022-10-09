import numpy

N, M = tuple(map(int, input().split()))

A = []
for _ in range(N):
    row = list(map(int, input().split()))
    A.append(row)

A_np = numpy.array(A)
    
print(numpy.mean(A, axis=1))
print(numpy.var(A, axis=0))
print(round(numpy.std(A), 11))

