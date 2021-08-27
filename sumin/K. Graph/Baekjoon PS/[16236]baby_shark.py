import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
size = [2, 2]
time = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            shark_point = (i, j)


def can_swimming(graph, row, col):
    global size
    direc = [(-1, 0), (0, -1), (0, 1), (-1, 0)]
    lst = []
    for r, c in direc:
        nr = row+r
        nc = col+c
        if 0 <= nr < n and 0 <= nc < n:
            if graph[nr][nc] <= size[0]:
                lst.append((nr, nc))
    return lst


def bfs_search(graph, row, col, visited):
    global size
    during_hunt = 0
    queue = deque()
    queue.append((row, col))
    while True:
        tqueue = deque()
        while queue:
            r, c = queue.popleft()
            if not visited[r][c]:
                visited[r][c] = True
                if 0 < graph[r][c] < size[0]:
                    if size[1] > 1:
                        size[1] -= 1
                    else:
                        size[1] = size[0]+1
                        size[0] += 1
                    graph[row][col] = 0
                    graph[r][c] = 9
                    print(r, c, during_hunt)
                    return (r, c, during_hunt)
                lst = can_swimming(graph, r, c)
                print(r, c, lst, size)
                if lst:
                    tqueue.extend(lst)
        if tqueue:
            queue = tqueue
        else:
            return False
        during_hunt += 1


while True:
    visited = [[False for _ in range(n)] for _ in range(n)]
    shark_point = bfs_search(graph, shark_point[0], shark_point[1], visited)
    if shark_point:
        time += shark_point[2]
    else:
        print(time, size)
        break

