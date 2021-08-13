n = int(input())
roads = list(map(int, input().split()))
cities = list(map(int, input().split()))
m = 1000000001
res = 0

for i in range(n-1):
    if cities[i] < m:
        m = cities[i]
        ind = i
for i in range(ind):
    res += roads[i]*cities[i]
res += sum(roads[ind:]) * m
print(res)
