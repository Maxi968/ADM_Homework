import re

S = input()
k = input()

if re.search(r'{}'.format(k), S):
    for w in re.finditer(r"(?=({}))".format(k), S):
        print("({}, {})".format(w.start(), w.end(1)-1))
else:
    print((-1, -1))
