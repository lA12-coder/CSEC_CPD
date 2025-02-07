n = int(input())
amt_of_cubes = list(map(int, input().split()))
amt_of_cubes.sort()
print(" ".join(map(str, amt_of_cubes)))