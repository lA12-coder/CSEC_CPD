num = int(input())
lst = list(map(int,input().split()))
Sereja = 0
Dima = 0
while len(lst)!=0:
    if lst[0] >= lst[-1]:
        Sereja+=lst[0]
        lst.remove(lst[0])
    else:
        Sereja += lst[-1]
        lst.remove(lst[-1])
    if len(lst) !=0:
        if lst[0] >= lst[-1]:
            Dima+=lst[0]
            lst.remove(lst[0])
        else:
            Dima += lst[-1]
            lst.remove(lst[-1])
    else:
        break
print(Sereja,Dima)

