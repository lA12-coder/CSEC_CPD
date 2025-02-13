s1, s2, s3, s4 = map(int, input().split())

horseshoes = {s1, s2, s3, s4}

duplicates = 4 - len(horseshoes)
print(duplicates)

