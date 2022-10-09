import re

pattern = "[A-Z]{2}[0-9]{3}[a-zA-Z0-9]{5}"

T = int(input())

for _ in range(T):
    uid = input()
    if len(uid)!=10:
        print("Invalid")
        continue
    chars = set(re.findall("\w", uid))
    if len(chars)!=10:
        print("Invalid")
        continue
    if re.search("[^\w]", uid)!=None:
        print("Invalid")
        continue
    digits = re.findall("[0-9]", uid)
    if len(digits)<3:
        print("Invalid")
        continue
    uppers = re.findall("[A-Z]", uid)
    if len(uppers)<2:
        print("Invalid")
        continue
    print("Valid")
