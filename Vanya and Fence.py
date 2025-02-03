n,h=map(int, input().split())
friends =list(map(int , input().split()))
w_list=[]
for x in friends:
    w_list.append(1) if x<=h else w_list.append(2)
w=sum(w_list)
print(w)