n = int(input())
count = 1
lst=[]
x = int(input())
lst.append(x)
for i in range(n-1):
    x = int(input())
    if lst[-1] == x:
        lst.append(x)
    else:
        count+=1
        lst.clear()
        lst.append(x)

print(count)