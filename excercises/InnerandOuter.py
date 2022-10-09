import numpy

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_np = numpy.array(A)
B_np = numpy.array(B)

print(numpy.inner(A_np, B_np))
print(numpy.outer(A_np, B_np))

