

# Complete the solve function below.
def solve(s):
    words = s.split(" ")
    res=[]
    for w in words:
        res.append(w.capitalize())
    return " ".join(res)
