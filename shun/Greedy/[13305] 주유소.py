N = int(input())
dis=list(map(int,input().split()))
cost=list(map(int,input().split()))

min = cost[0]
sum = 0
for i in range(N-1):
    if min > cost[i]:
        min = cost[i]
    sum+=(min * dis[i])
print(sum)
