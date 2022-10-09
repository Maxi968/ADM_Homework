S = input()


def sort_string(c):
    if c.islower():
        return (-1, c)
    elif c.isupper():
        return (0, c)
    elif c.isdigit():
        if int(c)%2==0:
            return (2, c)
        else:
            return (1, c)

res = sorted(S, key=sort_string)
print("".join(res))
