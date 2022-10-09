A = set(map(int, input().split(" ")))
n = int(input())
res = True

for i in range(n):
    ins = set((map(int, input().split(" "))))
    if A.union(ins)==A and A!=ins:
        continue
    else:
        res = False
        break

print(res)
