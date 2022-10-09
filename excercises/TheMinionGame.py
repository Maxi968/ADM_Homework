def minion_game(string):
    k = 0
    vowels = "AEIOU"
    for i in range(len(string)):
        if string[i] in vowels:
            k+=len(string)-i
    
    s=int(len(string)*(len(string)+1)/2)-k
    
    if s>k: 
        print('Stuart', s)
        return
    elif k > s:
        print('Kevin', k)
    else:
        print('Draw')

