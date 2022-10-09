if __name__ == '__main__':
    s = input()
    alpha = False
    digit = False
    alnum = False
    low = False
    up = False
    
    for char in s:
        if not alpha:
            alpha = char.isalpha()
        if not digit:
            digit = char.isdigit()
        if not alnum:
            alnum = char.isalnum()
        if not low:
            low = char.islower()
        if not up:
            up = char.isupper()
    
    print(alnum)
    print(alpha)
    print(digit)
    print(low)
    print(up)
    
