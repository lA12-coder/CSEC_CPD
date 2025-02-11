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

<<<<<<< HEAD
print(count)
=======
print(count)
>>>>>>> 2022e78abe94c566f21705f1802f77989c991ec4
