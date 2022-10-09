res=0
n_m = input().split()
array = input().split()
A = set(input().split())
B = set(input().split())
for el in array:
    if el in A: 
        res+=1
    if el in B: 
        res-=1
print(res)
