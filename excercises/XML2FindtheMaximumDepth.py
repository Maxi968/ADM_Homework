

maxdepth = 0
def depth(elem, level):
    global maxdepth
    if (level==maxdepth):
        maxdepth+=1
    for tag in elem:
        depth(tag, level+1) 

