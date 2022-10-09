if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    l_comb = [[i,j,k] for k in range(z+1) for j in range(y+1) for i in range(x+1)]
    
    res = [comb for comb in l_comb if sum(comb)!=n]
    
    print(sorted(res))
