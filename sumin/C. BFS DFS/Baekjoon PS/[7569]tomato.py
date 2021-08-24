from collections import deque
import sys

input = sys.stdin.readline


col, row, height = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(row)] for _ in range(height)]


def can_corruption(graph, height, row, col, mh, mr, mc):
    direc = [(0, 1, 0), (0, -1, 0), (0, 0, 1),
             (0, 0, -1), (1, 0, 0), (-1, 0, 0)]
    temp = []
    for h, r, c in direc:
        nh = height+h
        nr = row+r
        nc = col+c
        if 0 <= nh < mh and 0 <= nr < mr and 0 <= nc < mc:
            if graph[nh][nr][nc] == 0:
                temp.append((nh, nr, nc))
    for h, r, c in temp:
        graph[h][r][c] = 1
    if temp:
        return temp
    else:
        return False


def bfs_search(graph):
    queue = deque()
    day = -1
    for i in range(height):
        for j in range(row):
            for k in range(col):
                if graph[i][j][k] == 1:
                    queue.append((i, j, k))
    while True:
        day += 1
        temp = []
        while queue:
            h, r, c = queue.popleft()
            res = can_corruption(graph, h, r, c, height, row, col)
            for floor in graph:
                for wid in floor:
                    print(wid)
            print(res)
            print()
            if res:
                temp.extend(res)
            else:
                for i in range(height):
                    for j in range(row):
                        for k in range(col):
                            if graph[i][j][k] == 0:
                                return -1
                return day
        queue.extend(temp)


print(bfs_search(box))
