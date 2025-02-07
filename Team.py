n = int(input())
solved = 0
ls = []
for i in range(n):
    x = tuple(map(int, input().split()))
    ls.append(x)
for x in ls:
    if x.count(1)>=2:
        solved +=1
print(solved)

