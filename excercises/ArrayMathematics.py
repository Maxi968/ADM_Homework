import numpy

N, M = tuple(map(int, input().split()))

A=[]
B=[]

for _ in range(N):
    A.append(numpy.array(list(map(int, input().split()))))
    
for _ in range(N):
    B.append(numpy.array(list(map(int, input().split()))))

print(numpy.add(A,B))
print(numpy.subtract(A,B))
print(numpy.multiply(A,B))
print(numpy.floor_divide(A,B))
print(numpy.mod(A,B))
print(numpy.power(A,B))





