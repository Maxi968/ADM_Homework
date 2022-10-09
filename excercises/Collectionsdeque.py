from collections import deque

d = deque()

N = int(input())

for _ in range(N):
    method, *index = input().split()
    getattr(d, method)(*index)  
      
print(*d, sep=' ')
