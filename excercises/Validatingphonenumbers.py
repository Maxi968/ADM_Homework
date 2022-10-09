import re

N = int(input())

pattern = "[789][0-9]{9}$"

for _ in range(N):
    number = input()
    if re.match(pattern, number):
        print("YES")
    else:
        print("NO")
