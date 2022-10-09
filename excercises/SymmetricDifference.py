
M=int(input())
inp = input().split()
a=set(list(map(int, inp)))

N=int(input())
inp = input().split()
b=set(list(map(int, inp)))

for x in sorted(a^b):
    print(x)
