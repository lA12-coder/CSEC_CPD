n = int(input())
uniforms = [tuple(map(int, input().split())) for _ in range(n)]

count = 0
for i in range(n):
    for j in range(n):
        if i != j and uniforms[i][0] == uniforms[j][1]:
            count += 1

print(count)

