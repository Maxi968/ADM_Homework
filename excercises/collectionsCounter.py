from collections import Counter

X = int(input())
list_shoes = list(map(int, input().split(" ")))
diz = Counter(list_shoes)
N = int(input())

res = 0

for i in range(N):
    order = input().split(" ")
    shoe_size = int(order[0])
    prize = int(order[1])
    if diz[shoe_size]>0:
        res+=prize
        diz[shoe_size]-=1
print(res)
        
    
