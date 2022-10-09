T = int(input())

for i in range(T):
    try:
        a,b = tuple(map(int, input().split(" ")))
        res = a//b
        print(res)
    except (ValueError, ZeroDivisionError) as error:
        print("Error Code:", error)

        

        
        
