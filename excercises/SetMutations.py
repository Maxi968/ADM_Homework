A_n = int(input())
lista = input()
lista = [int(n) for n in lista.split(" ")]
A = set(lista)
N_n = int(input())

for i in range(N_n):
    operazione = input()
    l = operazione.split(" ")
    operazione = l[0]
    numero_elementi = l[1]
    altra_lista = input()
    altra_lista = altra_lista.split(" ")
    l = [int(n) for n in altra_lista]
    B = set(l)
    if operazione=="intersection_update":
        A.intersection_update(B)
    elif operazione=="update":
        A.update(B)
    elif operazione=="symmetric_difference_update":
        A.symmetric_difference_update(B)
    elif operazione=="difference_update":
        A.difference_update(B)
    else:
        continue

print(sum(A))
    
    
