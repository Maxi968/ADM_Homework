def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        res=''
        for j in range(i, i+k):
            if string[j] not in res:
                res+=string[j]
        print(res)

