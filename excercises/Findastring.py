def count_substring(string, sub_string):
    s = ""
    res = 0
    for i in range(len(string)):
        if i+len(sub_string)<=len(string):
            for j in range(i, i+len(sub_string)):
                s+=string[j]
            if s==sub_string:  
                res+=1
            s=""
    return res

