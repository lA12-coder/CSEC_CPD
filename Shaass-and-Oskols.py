n = int(input())
birds = list(map(int, input().split()))

m = int(input())

for i in range(m):
    x, y = map(int, input().split())
    x -= 1 # Convert to 0-based index

    if x > 0:
        birds[x - 1] += y - 1
    if x < n - 1:
        birds[x + 1] += birds[x] - y
    birds[x] = 0

for bird in birds:
    print(bird)
