if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    ins = set(arr)
    ins.remove(max(ins))
    print(max(ins))
