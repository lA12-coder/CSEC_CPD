no_events = int(input())
events = list(map(int,input().split()))
untreated = 0
available_officers = 0

for event in events:
    if event == -1:
        if available_officers >0:
            available_officers -= 1
        else:
            untreated +=1
    else:
        available_officers += event


print(untreated)