n = int(input())

food_cage = list(map(int, input().split()))

d = [0] * 101
d[1] = food_cage[0]
d[2] = max(d[1], food_cage[1])

for i in range(3, n + 1):
    d[i] = max(d[i - 1], d[i - 2] + food_cage[i - 1])

print(d[n])