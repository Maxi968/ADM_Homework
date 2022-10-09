N = int(input())

l = []

for _ in range(N):
    string = input().split()
    method = string[0]
    if method=="print":
        print(l)
    else:
        method+="("+",".join(string[1:])+")"
        eval("l."+method)
    
