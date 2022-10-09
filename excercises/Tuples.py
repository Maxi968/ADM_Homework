if __name__ == '__main__':
    n = int(input())
    int_list = input().split()
    t = tuple(map(int, int_list))
    print(hash(t))
