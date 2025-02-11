a1, a2, a3, a4 = map(int, input().split())
s = input().strip()
x = 0
calorie_map = {
    '1': a1,
    '2': a2,
    '3': a3,
    '4': a4
}
for char in s:
    x += calorie_map[char]
print(x)