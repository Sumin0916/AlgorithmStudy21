import sys
from collections import deque

input = sys.stdin.readline


def can_move(r1, c1, r2, c2):
    for i in range(4):
        nr1 = dx[i] + r1, nc1 = dy[i] + c1
        nr2 = dx[i] + r2, nc2 = dy[i] + c2
        if 0 <= nr < N and 0 <  = nc < M:
            if graph[nr][nc] == ".":
                

def bfs_search(start_info):
    queue = deque()
    queue.append(start_info)
    visited = [list(False for _ in range(M)) for _ in range(N)]
    visited[start_info[0][0]][start_info[0][1]] = True
    while queue:
        rr, rc, br, bc = queue.popleft()
        

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(N)]
start_point = [None, None]

for i in range(N):
    for j in range(M):
        if graph[i][j] == "B":
            start_point[1] = [i, j]
        elif graph[i][j] == "A":
            start_point[0] = [i, j]



