word = input().strip()
upper = []
lower =[]
for x in word:
    if x.isupper():
        upper.append(x)
    else:
        lower.append(x)

if len(upper)>len(lower):
    word = word.upper()
    print(word)
elif len(upper)<len(lower):
    word = word.lower()
    print(word)
else:
    word = word.lower()
    print(word)


