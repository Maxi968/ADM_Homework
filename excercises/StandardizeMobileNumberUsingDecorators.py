def wrapper(f):
    def fun(l):
        prefix = "+91"
        list_ = []
        for n in l:
            res = prefix+" "+n[-10:-5]+" "+n[-5:]
            list_.append(res)
        f(list_)
    return fun

