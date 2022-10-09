import numpy

N = int(input())

A=[]
B=[]
for _ in range(N):
   row = list(map(int, input().split()))
   A.append(row)

for _ in range(N):
   row = list(map(int, input().split()))
   B.append(row)
   
A_np = numpy.array(A)
B_np = numpy.array(B)

print(numpy.dot(A_np, B_np))
