import numpy

N, M, P = tuple(list(map(int, input().split())))

matrix_np=[]
matrix_mp=[]

for _ in range(N):
    column = list(map(int, input().split()))
    matrix_np.append(column)

for _ in range(M):
    column = list(map(int, input().split()))
    matrix_mp.append(column)

np_np = numpy.array(matrix_np)
np_mp = numpy.array(matrix_mp)

print(numpy.concatenate((np_np, np_mp), axis=0))
