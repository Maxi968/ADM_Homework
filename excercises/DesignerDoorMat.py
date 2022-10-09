N, M = map(int, input().split())
for n in range(N//2):
    print(('.|.'* (2*n + 1)).center(M, '-'))
print('WELCOME'.center(M, '-'))
for n in reversed(range(N//2)):
    print(('.|.'* (2*n + 1)).center(M, '-'))
