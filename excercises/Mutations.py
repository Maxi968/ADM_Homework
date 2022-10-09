def mutate_string(string, position, character):
    list_string = list(string)
    list_string[position]=character
    res = ("").join(list_string)
    
    return res

