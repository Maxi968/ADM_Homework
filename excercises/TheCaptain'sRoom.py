K = int(input())
room_list = input().split(" ")
rooms = [int(x) for x in room_list]
diz = {}

for room in rooms:
    if room in diz:
        diz[room]+=1
    else:
        diz[room]=1
        
for k,v in diz.items():
    if v==1:
        res=k
        break
print(res)
