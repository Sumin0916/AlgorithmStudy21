import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
size = 2
time = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            shark_point = (i, j)


def can_swimming(graph, row, col):
    global size
    direc = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    lst = []
    for r, c in direc:
        nr = row+r
        nc = col+c
        if 0 <= nr < n and 0 <= nc < n:
            if graph[nr][nc] <= size:
                lst.append((nr, nc))
    return lst


def bfs_search(graph, row, col):
    global size
    during_hunt = 0
    queue = deque()
    queue.append((row, col))
    while True:
        tqueue = []
        during_hunt += 1
        while queue:
            r, c = queue.leftpop()
            if graph[r][c] < size:
                size += 1
                graph[r][c] = 0
                return (r, c, during_hunt)
            lst = can_swimming(graph, r, c)
            if lst:
                tqueue.append(lst)
        queue = tqueue
    return False


while True:
    shark_point = bfs_search(graph, shark_point[0], shark_point[1])
    if shark_point:
        time += shark_point[2]
    else:
        print(time)
        break

