import heapq

N = int(input())
K = int(input())

lst = []

for i in range(1, N+1):
    for j in range(1, N+1):
        heapq.heappush(lst, i*j)

for _ in range(N*N):
    print(heapq.heappop(lst), end=" ")

