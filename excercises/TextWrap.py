

def wrap(string, max_width):
    l=[]
    for i in range(0,len(string),max_width):
        l.append(string[i:i+max_width])
    res="\n".join(l)
    return res       

