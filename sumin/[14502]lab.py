import sys
from collections import deque
import copy
# 빡구현 문제 어지럽다
input = sys.stdin.readline
res = 0

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
is_cons = [list(False for _ in range(M)) for _ in range(N)]
direc = [[1, 0], [-1, 0], [0, 1], [0, -1]]
queue = deque()

for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            queue.append([i, j])
            is_cons[i][j] = True
        elif graph[i][j] == 1:
            is_cons[i][j] = True


def can_pollution(queue, graph):  # 바이러스 좌표가 담긴 큐를 받아 앞으로 감염될 좌표를 반환한다.(미리 지도상에는 감염시켰다 표기)
    tqueue = deque()
    while queue:
        row, col = queue.popleft()
        for r, c in direc:
            nr = row + r
            nc = col + c
            if 0 <= nr < N and 0 <= nc < M:
                if graph[nr][nc] == 0:
                    tqueue.append([nr, nc])
                    graph[nr][nc] = 2
    return tqueue


def bfs(queue, graph):  # 큐를 받아 끝까지 감염시켜보고 안전 지역 범위를 반환한다.
    area = 0
    while queue:
        queue = can_pollution(queue, graph)
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                area += 1
    return area


def combination(start, count):  # 받은 현재 좌표에서 3개를 고를 수 있는 인덱스를 반환한다.
    global res
    if count == 3:
        tgraph = copy.deepcopy(graph)
        tqueue = copy.deepcopy(queue)
        res = max(res, bfs(tqueue, tgraph))
    else:
        for i in range(start, N*M):
            r = i // M
            c = i % M
            if graph[r][c] == 0:
                graph[r][c] = 1
                combination(start+1, count+1)
                graph[r][c] = 0


combination(0, 0)
print(res)

