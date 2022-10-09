N = int(input())

starts = "456"

for _ in range(N):
    card_n = input()
    if card_n[0] not in starts:
        print("Invalid")
        continue
    if "-" in card_n:
        if card_n[4]!="-" or card_n[9]!="-" or card_n[14]!="-":
            print("Invalid")
            continue
        if len(card_n)!=19:
            print("Invalid")
            continue
    else:
        if len(card_n)!=16:
            print("Invalid")
            continue
    card_n = card_n.replace("-","")
    for n in card_n:
        if not n.isdigit():
            print("Invalid")
            continue
    valid = True
    for i in range(len(card_n)):
        group = card_n[i:i+4]
        if len(group)!=4:
            break
        numbers = set(group)
        if len(numbers)==1:
            valid = False
            break
    if not valid:
        print("Invalid")
        continue
    print("Valid")
        
    
