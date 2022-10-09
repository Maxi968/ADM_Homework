N = int(input())
cols = input().split()

marks=[]
for _ in range(N):
    marks.append(int(input().split()[cols.index('MARKS')]))

print(sum(marks)/len(marks))
