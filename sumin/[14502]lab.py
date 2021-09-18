import sys
from collections import deque

input = sys.stdin.readline
queue = deque()
res = 0

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
is_cons = [list(False for _ in range(M)) for _ in range(N)]

direc = [[1, 0], [-1, 0], [0, 1], [0, -1]]

for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            queue.append([i, j])
            is_cons[i][j] = True
        elif graph[i][j] == 1:
            is_cons[i][j] = True


