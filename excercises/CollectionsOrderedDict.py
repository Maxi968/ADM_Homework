N = int(input())
diz={}

for i in range(N):
    inp = input().split()
    item = " ".join(inp[:-1])
    price = int(inp[-1])
    diz[item] = price+diz.get(item, 0)

for k, v in diz.items():
    print(k, v)
