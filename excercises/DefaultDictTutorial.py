from collections import defaultdict 
diz = defaultdict(list)

N, M = tuple(map(int, input().split()))

for i in range(1, N+1):
    inp = input()
    diz[inp].append(i)
    
for _ in range(M):
    inp = input()
    if inp in diz.keys():
        print(*diz[inp])
    else:
        print(-1)
