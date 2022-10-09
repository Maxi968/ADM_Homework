import re

pattern = r"([#][abcdefABCDEF0-9]{6})|([#][abcdefABCDEF0-9]{3})"

N = int(input())

text = ""

for _ in range(N):
    text+=input() 

valid = [p.split('}')[0] for p in text.split('{') if '}' in p]

for string in valid:
    res = re.findall(pattern, string)
    for tupla in res:
        for el in tupla:
            if el:
                print(el)
    


    
