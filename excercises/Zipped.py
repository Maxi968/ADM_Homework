N, X = tuple((map(int, input().split(" "))))
    
list_marks=[]

for _ in range(X):
    marks = input().split(" ")
    list_marks.append(marks)

students_marks = list(zip(*list_marks))

avg_list = []

for tupla in students_marks:
    t = tuple(map(float, tupla))
    avg = sum(t)/len(t)
    print(avg)
