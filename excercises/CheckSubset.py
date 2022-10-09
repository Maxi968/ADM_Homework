T = int(input())

for i in range(T):
    A_e = int(input())
    A = set(map(int, input().split(" ")))
    B_e = int(input())
    B = set(map(int, input().split(" ")))
    
    if A.union(B)==B:
        print(True)
    else:
        print(False)

        
