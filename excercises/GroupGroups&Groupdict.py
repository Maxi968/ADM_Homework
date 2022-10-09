import re

string = input()
match = re.search(r"([a-zA-Z0-9])\1+", string)
if match:
    print(match.group()[0])
else:
    print(-1)
