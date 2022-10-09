import re

N = int(input())

for _ in range(N):
    t = input()
    res = re.sub(r"(?<=\s)(&&)(?=\s)", "and", t)
    res2 = re.sub(r"(?<=\s)(\|\|)(?=\s)", "or", res)
    print(res2)
