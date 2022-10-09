if __name__ == '__main__':
    
    diz = {}
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        diz[name]=score
    
    min_score = min(diz.values())
    diz2={}
    
    for k,v in diz.items():
        if v!=min_score:
             diz2[k]=v
    
    second_min_score = min(diz2.values())
    students=[]
    
    for k,v in diz2.items():
        if v==second_min_score:
            students.append(k)
    
    students = list(sorted(students))
    
    for s in students:
        print(s)
        
