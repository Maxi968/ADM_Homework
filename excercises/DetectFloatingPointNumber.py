import re

N = int(input())


for _ in range(N):
    string = input()
    if re.search("^[-+]?\d*[.]\d*$", string):
        print(True)
    else:
        print(False)

""" ^[-+]?\d*[.]\d*$ """
