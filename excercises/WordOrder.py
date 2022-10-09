diz={}
N = int(input())

for _ in range(N):
    word = input()
    diz[word] = diz.get(word, 0)+1
print(len(diz))

str_values = [str(x) for x in diz.values()]
res = " ".join(str_values)

print(res)
