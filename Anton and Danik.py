n = input()
s = input().strip()
A = 0
D = 0
for x in s:
    if x == "A":
        A+=1
    else:
        D+=1
if A>D:
    print('Anton')
elif A<D:
    print("Danik")
else:
    print("Friendship")


