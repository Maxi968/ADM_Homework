import re

S = input()

list_res = re.findall(r'(?<=[^aeiou])([aeiou]{2,})(?=[^aeiou])', S, flags=re.IGNORECASE)

if len(list_res)==0:
    print(-1)
else:
    for w in list_res:
        print(w)
