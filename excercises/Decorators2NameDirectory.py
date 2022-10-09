

def person_lister(f):
    def inner(people):
        l=[]
        res = sorted(people, key=ordina)
        for person in res:
           l.append(f(person))
        return l
    return inner

def ordina(person):
    return int(person[2])
    
