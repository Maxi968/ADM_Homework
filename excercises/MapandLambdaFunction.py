cube = lambda x : x**3

def fibonacci(n):
    return [fibonacci_list(x) for x in range(n)]    


def fibonacci_list(n):
    if n==0:
        return 0 
    elif n==1:
        return 1
    else:
        return fibonacci_list(n-1)+fibonacci_list(n-2)


