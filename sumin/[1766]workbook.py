import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
num_edge = [0 for _ in range(N+1)]
check = [0 for _ in range(N+1)]
edge = []
num_edge[0] = -1
for _ in range(M):
    a, b = map(int, input().split())
    num_edge[b] += 1
    check[a] = 1
    edge.append([a, b])
for i in check[1:]:
    if not i:
        edge.append([i, i+1])
edge.sort(key=lambda x: x[1])
print(edge)
lst = deque([x for x in range(1, N+1) if not num_edge[x]])

while lst:
    a = lst.popleft()
    print(a)
